def escape_json(text: str) -> str:
    return text.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", "\\n").replace("\r", "")

def main():
    print("=== JSONL Formatter for Summaries ===")

    while True:
        transcript = input("Enter transcript (single line), or 'exit' to quit:\n")
        if transcript.strip().lower() == "exit":
            break

        print("Enter summary (multi-line). Type 'END' on its own line to finish:")
        summary_lines = []
        while True:
            line = input()
            if line.strip() == "END":
                break
            summary_lines.append(line)
        summary = "\n".join(summary_lines)

        transcript_escaped = escape_json(transcript)
        summary_escaped = escape_json(summary)

        json_line = (
            f'{{"instruction": "Summarize the following text into a structured lesson with clear, concise paragraphs.", '
            f'"input": "{transcript_escaped}", '
            f'"output": "{summary_escaped}"}}'
        )

        print("\n--- JSONL Entry ---")
        print(json_line)
        print("-------------------\n")

    print("Exiting...")

if __name__ == "__main__":
    main()