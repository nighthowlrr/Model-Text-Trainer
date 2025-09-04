# Project Structure

```
Model-Text-Trainer/
│── .aiassistant/
│   └── rules/
│       ├── General-rules.md
│       └── Project-rules.md
│── code_util/
│   ├── __init__.py
│   └── file_pickers.py
│── gguf/ (IN PROGRESS)
│   ├── __init__.py
│   ├── quantize_to_gguf.py
│   └── convert_to_gguf.py
│── inference/
│   ├── __init__.py
│   ├── inference.py
│   └── inference_gguf.py
│── train/
│   ├── __init__.py
│   ├── merge_lora.py
│   └── train_lora.py
│── utils/
│   ├── __init__.py
│   ├── download_model.py
│   ├── jsonl_interactive.py
│   └── validate_jsonl.py
│── notes/
│   ├── Detailed-To-Do.md
│   ├── Evaluation-Pipeline-GPT-Explain.md
│   └── Project-Structure.md
│── manage_wheels.py (IN PROGRESS)
│── .editorconfig
│── LICENSE
│── pyproject.toml
│── README.md
└── requirements.txt
```