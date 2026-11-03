# Quickstart

## Prerequisites
- Python 3.15
- Project dependencies installed according to the repository workflow

## Validate the CLI behavior

### 1) Convert Markdown from standard input
```bash
printf '%s
' '| a | b |' '|---|---|' '| 1 | 2 |' | uv run --locked --offline python -m md2csv
```

**Expected outcome**: CSV is printed to standard output with one header row and one data row.

### 2) Convert Markdown from a file
```bash
uv run --locked --offline python -m md2csv path/to/sample.md
```

**Expected outcome**: The first valid Markdown table in the file is converted to CSV output.

### 3) Verify no-table handling
```bash
printf '%s
' 'This file has no table.' | uv run --locked --offline python -m md2csv
```

**Expected outcome**: The command exits non-zero and prints a clear error message indicating that no valid Markdown table was found.

### 4) Verify escaped pipes and empty cells
```bash
printf '%s
' '| a | b | c |' '|---|---|---|' '| x\\|y | | z |' | uv run --locked --offline python -m md2csv
```

**Expected outcome**: Escaped pipe content remains in a single cell, empty cells are preserved, and CSV output has the correct column count.

## Notes
- See `research.md` for parser and error-handling decisions.
- See `data-model.md` for the table and CSV output flow.
