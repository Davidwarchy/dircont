# dircont

**dircont** is a simple CLI tool for recursively reading and concatenating code files (like `.py`, `.md`, etc.) from a directory into a single output file. It's useful for documentation, code review, archiving, or preparing code for large language models.

## ✨ Features

- Concatenates all files of specified extensions from a directory
- Recursively includes files from subdirectories
- Adds file headers for traceability
- Supports multiple formats: `.py`, `.txt`, `.md`, etc.
- Simple and fast to use

## 📦 Installation

Clone the repo and install in **editable mode**:

```bash
git clone https://github.com/davidwarchy/dircont.git
cd dircont
pip install -e .
```

This makes the `dircont` command available globally.

> ⚠️ Requires Python 3.6+

## 🚀 Usage

```bash
dircont -i . 
``` 

The above will concatenate all python files into a single output file `x.markdown`, saved in the current directory. 

```bash
dircont -i <input_directory> [-o <output_file>] [-f <extensions>...]
```

### Arguments

| Flag            | Description                                          | Default       |
|-----------------|------------------------------------------------------|---------------|
| `-i`, `--input` | Directory to search for files                        | **Required**  |
| `-o`, `--output`| Name of the output file                              | `x.markdown`  |
| `-f`, `--formats`| File extensions to include (e.g., `.py .md .txt`)   | `.py`         |

### Example

Concatenate all `.py`, `.md`, and `.txt` files into `combined.md`:

```bash
dircont -i ./myproject -o combined.md -f .py .md .txt
```

## 🛠 Project Structure

```
dircont/
├── dircont/
│   └── main.py        # CLI logic
├── pyproject.toml     # Project config
├── README.md
```

## ✍️ Author

**David Warutumo**  
📧 davidwarchy@gmail.com

## 📄 License

MIT 