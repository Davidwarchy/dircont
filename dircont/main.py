import os
import argparse

def read_files_by_extension(directory, output_file, extensions):
    with open(output_file, "w", encoding="utf-8") as out:
        for root, _, files in os.walk(directory):
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
        description="Concatenate specified types of files from a folder into one text file."
    )
    parser.add_argument(
        "-i", "--input", default=".", help="Input directory. Default: current directory"
    )
    parser.add_argument(
        "-o", "--output", default="x.markdown", help="Output file name. Default: x.markdown"
    )
    parser.add_argument(
        "-f", "--formats", nargs="+", default=[".py"],
        help="File extensions to include (e.g., .py .txt .md). Default: .py"
    )

    args = parser.parse_args()
    read_files_by_extension(args.input, args.output, args.formats)

if __name__ == "__main__":
    main()
