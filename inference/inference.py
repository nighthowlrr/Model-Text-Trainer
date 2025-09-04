import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

from code_util.file_pickers import pick_folder, pick_file

def main():
    parser = argparse.ArgumentParser(description="Run inference with a HuggingFace model (fine-tuned or base).")
    parser.add_argument("--model_dir", type=str, help="Path to HuggingFace model folder")
    parser.add_argument("--input_file", type=str, help="Path to text file containing transcript to summarize")
    args = parser.parse_args()

    model_dir = args.model_dir or pick_folder("Select HuggingFace model folder")
    input_file = args.input_file or pick_file("Select transcript text file")

    with open(input_file, "r", encoding="utf-8") as f:
        transcript = f.read()

    print("=== Loading model and tokenizer ===")
    tokenizer = AutoTokenizer.from_pretrained(model_dir)
    model = AutoModelForCausalLM.from_pretrained(model_dir, dtype=torch.float16, device_map="auto")

    summarizer = pipeline("text-generation", model=model, tokenizer=tokenizer,
                          device=0 if torch.cuda.is_available() else -1)

    prompt = f"Summarize the following lesson transcript:\n\n{transcript}\n\nSummary:"

    print("=== Running inference ===")
    output = summarizer(prompt, max_length=1024, do_sample=False)[0]["generated_text"]

    print("\n=== Summary ===\n")
    print(output)


if __name__ == "__main__":
    main()