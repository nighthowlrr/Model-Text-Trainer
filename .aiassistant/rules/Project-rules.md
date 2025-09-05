---
apply: always
---

# Project-Specific Script Guidelines

Begin with a concise checklist (3–7 bullets) of what you will do; keep items conceptual, not implementation-level.

- **Self-contained Scripts**: Ensure each script is fully independent within the project. Do not rely on other scripts unless absolutely necessary and, in such cases, obtain prior confirmation.
- **Single Responsibility**: Each script should perform only one task to maintain clarity and simplicity.
- **Minimal System Dependencies**: Avoid reliance on system-wide tools (e.g., `cmake`, `make`, global Python packages). All dependencies must be managed and installed locally from within the project directory (e.g., via `requirements.txt`).
- **Prefer Python Packages**: Use Python dependencies specified in `requirements.txt` whenever possible instead of calling external binaries. Only use binaries if a Python alternative does not exist, and confirm this first.
- **Path Handling**:
  - Do not hardcode paths in any script intended for user interaction. Prompt users or accept paths as CLI arguments.
  - Hardcoded paths are only permissible in utility scripts not aimed at direct user interaction.
- **CLI Argument Standards**:
  - Support a `--help` flag in all scripts with CLI arguments, providing concise and clear documentation.
  - Scripts should be runnable without CLI arguments; when invoked this way, interactively prompt for required input.
  - Any script that requests user input must also allow that input to be provided via CLI arguments.
- **Interface Simplicity**: Keep CLI arguments and user prompts minimal and straightforward.
- **Input Visibility**: Before starting, print all input values, clearly separated from process logs by a line of equal signs (e.g., `print("============")`).
- **User Logging**: For scripts running lengthy processes, log progress visibly to the console. Indicate total steps and the current step (e.g., `print("1/4: Loading model and LoRA adapter")`).
- **Completion Logging**: Do not log after each step—only print a completion message when the full process has completed successfully.

After each script change or addition, validate that all guidelines are followed in 1-2 lines; if any are not, correct before proceeding.