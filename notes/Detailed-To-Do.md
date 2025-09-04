# Detailed To-do List

## Version 1.0.0 (First Version)
- [X] Script for training LoRA adapters on custom `training_data.jsonl`
- [X] Utility script for entering raw training data to get a `.JSONL` entry
- [X] Utility script for detecting syntax errors in `training_data.jsonl`
- [X] Script for merging LoRA adapters with the base model to get a trained model in HuggingFace format.
- [X] Utility script to download model from HuggingFace library
- [X] Script for running inference of a trained HuggingFace model.
- [ ] Script for converting a HuggingFace format model into GGUF format. (*IN PROGRESS*)
- [ ] Script for quantizing a GGUF model to lower precision for efficient CPU/GPU inference. (*IN PROGRESS*)
- [X] Script for running inference of a GGUF model.

## Version 1.1.0
- [ ] Add `main.py` entry-point script to run other scripts through inputting a number to select an option. (*NEXT*)
- [ ] Improve `validate_jsonl.py` to not only detect but also automatically fix syntax errors in `training_data.jsonl`. 
  - User will have the option (through CLI arg or script input) to either check or to fix syntax errors
- [ ] `defaults.yaml` Default configuration file for easily running the whole workflow without manually entering arguments everytime.
  - Scripts will follow this pattern: `CLI args > defaults.yaml > user input` (user input when no defaults and args provided)

## Proposed Features
- [ ] Support for distributed training on multiple GPUs. 
- [ ] Add an evaluation pipeline (ROUGE, BLEU) for summaries output by the model.
  - Explained (by ChatGPT) in more detail in [these notes](Evaluation-Pipeline-GPT-Explain.md)
- [ ] Add JSON schema validation to be followed by `training_data.jsonl` during data prep.
  - Additional layer of validating `training_data.jsonl` on top of `validate_jsonl.py` script.
  - Benefit: Enforces structure and field types for `training_data.jsonl`

