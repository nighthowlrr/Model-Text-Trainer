---
apply: always
---

# Project-specific Rules
- All scripts must be self-contained inside the project, meaning no script must rely on another script in the project to complete its task, unless absolutely necessary, and even then, first confirm from me beforehand.
- Each script must be about only one task. No script should handle multiple tasks, and that increases the complexity of the script, and we value simplicity in this project.
- Always try to have minimal reliance on system-wide installations or packages (e.g., cmake, make, global Python packages). 
- Everything must run from inside the project directory (Python dependencies in requirements.txt).
- Always prefer Python dependencies when available instead of shelling out to binaries. Always confirm that a dependency isn't available before choosing to shell out to binaries.
- Never hardcode paths, unless it's a utility script that will not be used by a user (e.g., a custom python script that downloads and installs `.whl` of python dependencies for the project). For scripts that will be used by a user, always ask the user or accept CLI args.
- Every script that accepts CLI args must support --help with concise but clear argument docs.
- Every script that accepts CLI args must be able to run without any arguments, and the script should ask the user for that input.
- Similarly, every script that asks a user for input must also have CLI args to take user input directly from the command line
- Always try to have as few CLI args or user queries per script as possible. This project is supposed to be extremely easy to use.
- Every script that accepts CLI args or asks the user for input must print to the console the input given before starting the process. 
- The chosen input print statements should be separated from the process logs by a line of equal signs. (e.g., `print("============")`)
- Every script that runs a lengthy process must print logs to the console so the user is informed about the status of the process. And the logs must also have the number of total steps and which step the process is currently on. (e.g., `print("1/4: Loading model and LoRA adapter")`).
- DO NOT print logs saying that a single step is done. Only show a completion message when the whole process has completed successfully.