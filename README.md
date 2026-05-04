# dircont

Concatenate files in a directory into a single markdown file.

## Installation

```bash
pip install -e .
```

## Usage

```bash
dircont
```

Default behavior:

- input: `.`
- output: `x.markdown`
- formats: `.md .py`
- ignores: `output/ .git __pycache__/ venv/ .venv/`

Equivalent to:

```bash
dircont -i . -o x.markdown -f .md .py
```

## Options

```bash
dircont -i my_project
dircont -o output.md
dircont -f .py .txt
dircont --ignore output logs data
```