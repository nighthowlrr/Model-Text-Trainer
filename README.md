# Model-Text-Trainer

## Overview
This portable project contains scripts for training, merging, and running inference with language models, 
specifically focusing on LoRA (Low-Rank Adaptation) fine-tuning.

This was created for training models to summarize text in my personal style of writing, 
but this can be used to train any model using any `.JSONL` training file.

## Key Features
- **LoRA Fine-tuning**: Script for training LoRA adapters to fine-tune language models on specific tasks. 
- **LoRA Merging**: Script for merging trained LoRA adapters into the base language model.
- **HuggingFace Inference**: Support for running inference directly with HuggingFace format models.
- **GGUF Conversion and Quantization**: (*IN PROGRESS*)
  - Script for converting HuggingFace format models to GGUF format.
  - Script for quantizing GGUF models to lower precision for efficient CPU/GPU inference.
- **GGUF Inference**: Support for running inference with quantized GGUF models.


- **Download Models from HuggingFace**: Script for downloading models from HuggingFace.
- **.JSONL tools**: Scripts for turning data into `.JSONL` format, and validating your `training_data.JSONL` file.

## Design standards
- Python libraries are packaged as wheels, so if any library is removed from pip, the project will still run. (*IN PROGRESS*) 
- There is minimal reliance on system-wide tools and installations (e.g., CMake, Make, global python packages)
- Every script that accepts CLI args supports `--help` with clear argument docs.
- Every script that accepts CLI args can run without any arguments, as the script will ask the user for input.
- All scripts are self-contained inside the project and can run without other scripts.

---

## Prerequisites and Dependencies
- **Python**: Version 3.12.* is recommended.
- **pip**

The following packages are required for running the scripts, as listed in [`requirements.txt`](requirements.txt):
- `datasets == 4.0.0`, 
- `huggingface-hub == 0.34.4`, 
- `llama-cpp-python == 0.3.16`, 
- `peft == 0.17.1`, 
- `torch == 2.8.0`, 
- `transformers == 4.56.0`

## Installation & Setup Instructions
1. Clone the repository:
    ```
    git clone https://github.com/nighthowlrr/Model-Text-Trainer.git
    cd Model-Text-Trainer 
    ```
2. Create a virtual environment (recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3. Install required dependencies:
    ```
    pip install -r requirements.txt
    ```

## Usage
TODO

---

## Roadmap
A detailed roadmap is available [here](notes/Detailed-To-Do.md).

Task currently in progress:
- [ ] Script for converting a HuggingFace format model into GGUF format.
- [ ] Script for quantizing a GGUF model to lower precision for efficient CPU/GPU inference.

## Contributing
This is currently a personal project. Contributions are not being accepted at this time.

## License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Acknowledgements
This project leverages the following excellent open-source libraries:
* [PEFT](https://github.com/huggingface/peft) — Parameter-Efficient Fine-Tuning methods
* [Transformers](https://github.com/huggingface/transformers) — State-of-the-art machine learning models
* [PyTorch](https://pytorch.org/) — Deep learning framework
* [Datasets](https://github.com/huggingface/datasets) — Data processing for machine learning
* [Hugging Face Hub](https://github.com/huggingface/huggingface_hub) — Model and dataset repository
* [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) — Python bindings for llama.cpp

Special thanks to the HuggingFace team for their incredible ecosystem of ML tools.
