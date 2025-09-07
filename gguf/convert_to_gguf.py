import argparse
import subprocess
import sys

from code_util.file_pickers import pick_folder

def main():
    parser = argparse.ArgumentParser(description="Convert a merged Hugging Face model to GGUF using Unsloth.")
    parser.add_argument("--model_dir", type=str, help="Path to merged Hugging Face model directory")
    parser.add_argument("--quant", type=str, help="Quantization method (f16, q8_0, q4_k_m, etc.)")
    parser.add_argument("--output_dir", type=str, help="Path to save the GGUF model (file or directory)")
    args = parser.parse_args()

    model_dir = args.model_dir or pick_folder("Select folder with merged Hugging Face model...")
    quant = args.quant or input("Enter Quantization method (f16, q8_0, q4_k_m, etc.): ").strip()
    output_dir = args.output_dir or pick_folder("Select output directory...")

    print("Input values:")
    print(f"  Model dir: {model_dir}")
    print(f"  Output: {output_dir}")
    print(f"  Quantization: {quant}")
    print("============")

    print("1/1: Running gguf-converter CLI")
    subprocess.run([sys.executable, "-m", "gguf-converter.cli",
                    "--model", model_dir,
                    "--output", output_dir,
                    "--quant", quant], check=True)
    print("Conversion completed successfully!")

if __name__ == "__main__":
    main()