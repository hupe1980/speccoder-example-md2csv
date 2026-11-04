# Data Model: Markdown to CSV CLI

## Overview
This feature has no persistent storage. The data model describes the in-memory flow from raw input text to parsed Markdown table rows and CSV text output.

## Entities

### MarkdownInput
- **Purpose**: Represents raw Markdown text supplied from standard input or a file.
- **Fields**:
  - `text`: full input content as a string
  - `source`: optional human-readable source label such as `stdin` or a file path
- **Notes**:
  - Empty text is allowed at the input boundary and handled by validation.

### MarkdownTable
- **Purpose**: Represents one valid Markdown table selected from the input.
- **Fields**:
  - `headers`: ordered list of header cell strings
  - `rows`: ordered list of body rows, each row being an ordered list of cell strings
- **Constraints**:
  - Each row must contain the same number of cells as the header width.
  - Formatting noise such as surrounding pipes and extra outer spacing is removed during parsing.
  - Escaped pipe characters inside cells remain part of the cell content.

### CsvTable
- **Purpose**: Represents the emitted CSV content for a Markdown table.
- **Fields**:
  - `lines`: ordered list of CSV rows, each row serialized with RFC-style escaping as needed
- **Constraints**:
  - Column order must match the source table order.
  - Empty cells serialize as empty CSV fields.
  - Commas, quotes, and line breaks must be escaped according to CSV conventions.

## Transformations

### Input to MarkdownTable
1. Read text from stdin or a file.
2. Locate the first valid Markdown table in the text.
3. Normalize cell spacing and preserve escaped characters that belong to cell content.
4. Validate that every data row matches the table width.

### MarkdownTable to CsvTable
1. Serialize header cells first when present.
2. Serialize each body row in order.
3. Quote fields only when required by CSV rules.
4. Preserve empty values and embedded special characters.

## Error States
- **NoTableFound**: No valid Markdown table is present in the input.
- **UnreadableInput**: The file or standard input content cannot be read.
- **MalformedTable**: The table structure is inconsistent or invalid.

## Validation Notes
- The quickstart scenarios focus on a single-table conversion flow.
- Multiple table selection is intentionally limited to the first valid table until a later decision changes the behavior.