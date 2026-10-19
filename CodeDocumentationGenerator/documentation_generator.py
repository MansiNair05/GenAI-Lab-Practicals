
from pathlib import Path

source_file = Path("sample_program.py")
output_file = Path("README.md")

if not source_file.exists():
    print("Error: Source program not found.")

else:
    source_code = source_file.read_text(encoding="utf-8")

    print("===== SOURCE CODE =====")
    print(source_code)

    print("\nGenerate documentation using ChatGPT.")
    print("Copy the generated documentation below.")
    print("Enter a line containing only END to finish.")

    lines = []

    while True:
        try:
            line = input()
        except EOFError:
            break

        if line.strip() == "END":
            break

        lines.append(line)

    documentation = "\n".join(lines).strip()

    if documentation:
        output_file.write_text(
            documentation + "\n",
            encoding="utf-8"
        )
        print("\nDocumentation saved to README.md")
    else:
        print("Error: Documentation cannot be empty.")
