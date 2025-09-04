import argparse
from llama_cpp import Llama

from code_util.file_pickers import pick_file

def main():
    parser = argparse.ArgumentParser(description="Run inference with a GGUF model (quantized).")
    parser.add_argument("--model_file", type=str, help="Path to GGUF model file (quantized)")
    parser.add_argument("--input_file", type=str, help="Path to text file containing transcript to summarize")
    args = parser.parse_args()

    model_file = args.model_file or pick_file("Select GGUF model file")
    input_file = args.input_file or pick_file("Select transcript text file")

    with open(input_file, "r", encoding="utf-8") as f:
        transcript = f.read()

    print("=== Loading GGUF model with llama-cpp ===")
    llm = Llama(model_path=model_file, n_ctx=4096, n_threads=4)

    prompt = f"Summarize the following lesson transcript:\n\n{transcript}\n\nSummary:"

    print("=== Running inference ===")
    output = llm(prompt, max_tokens=1024, stop=["Summary:"])

    print("\n=== Summary ===\n")
    print(output["choices"][0]["text"])

if __name__ == "__main__":
    main()