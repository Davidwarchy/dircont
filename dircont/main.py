import os
import argparse

DEFAULT_FORMATS = [".md", ".py"]
DEFAULT_IGNORES = {"output", ".git", "__pycache__", "venv", ".venv"}


def read_files_by_extension(directory, output_file, extensions, ignore_dirs):
    with open(output_file, "w", encoding="utf-8") as out:
        for root, dirs, files in os.walk(directory):
            # prevent walking into ignored dirs
            dirs[:] = [d for d in dirs if d not in ignore_dirs]

            for file in files:
                if any(file.endswith(ext) for ext in extensions):
                    file_path = os.path.join(root, file)
                    out.write(f"#### {file_path}\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            out.write(f.read())
                    except Exception as e:
                        out.write(f"Error reading {file}: {e}\n")
                    out.write("\n\n")


def main():
    parser = argparse.ArgumentParser(
        description="Concatenate specified file types from a folder into one markdown file."
    )

    parser.add_argument(
        "-i", "--input",
        default=".",
        help="Input directory (default: current directory)"
    )

    parser.add_argument(
        "-o", "--output",
        default="x.markdown",
        help="Output file (default: x.markdown)"
    )

    parser.add_argument(
        "-f", "--formats",
        nargs="+",
        default=DEFAULT_FORMATS,
        help="File extensions to include (default: .md .py)"
    )

    parser.add_argument(
        "--ignore",
        nargs="*",
        default=list(DEFAULT_IGNORES),
        help="Directories to ignore"
    )

    args = parser.parse_args()

    read_files_by_extension(
        args.input,
        args.output,
        args.formats,
        set(args.ignore)
    )


if __name__ == "__main__":
    main()