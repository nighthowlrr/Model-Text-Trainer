import json
import argparse
from code_util.file_pickers import pick_file

def validate_jsonl():
    parser = argparse.ArgumentParser(description="Validate JSONL training file")
    parser.add_argument("--train_file", type=str, required=False, help="Location of training data file")
    args = parser.parse_args()

    jsonl_file = args.train_file or pick_file("Select training data file...", True, [("JSONL Files", "*.jsonl")])

    if jsonl_file is None:
        print("No training data file selected. Exiting...")
        exit(1)

    error_count = 0
    print(f"Validating {jsonl_file}...")

    with open(jsonl_file, "r") as f:
        for i, line in enumerate(f, start=1):
            try:
                json.loads(line)
            except Exception as e:
                error_count += 1
                print(f"ERROR line {i}: {e}")

    print(f"Validation complete! Errors found: {error_count}")

if __name__ == "__main__":
    validate_jsonl()