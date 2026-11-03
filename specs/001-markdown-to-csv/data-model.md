# Data Model

## Entities

### MarkdownTable
Represents one parsed Markdown pipe table extracted from input.

**Fields**
- `header_cells: list[str]` — ordered header values; may be empty if the source table has no header row.
- `body_rows: list[list[str]]` — ordered data rows, each row preserving column order.
- `source_index: int` — zero-based position of the selected table within the input stream/file.
- `raw_source: str` — original table text used for debugging and error reporting.

**Validation Rules**
- Must contain at least one row of cell data.
- Each parsed row must yield a consistent column count after trimming outer pipe delimiters.
- Escaped pipes (`\|`) must remain part of cell content, not split columns.
- Empty cells are valid and represented as empty strings.

**Relationships**
- Converts to exactly one `CsvTable`.

### CsvTable
Represents the serialized output form of a parsed Markdown table.

**Fields**
- `rows: list[list[str]]` — ordered CSV rows including headers when present.
- `header_included: bool` — indicates whether the first row originated from a Markdown header row.

**Validation Rules**
- Rows must be emitted in source order.
- Cell values must be passed through CSV escaping rules before serialization.
- Output must preserve the same column count as the source table.

**Relationships**
- Derived from one `MarkdownTable`.

## State / Flow

1. Read input from stdin or file.
2. Detect and extract the first valid Markdown table.
3. Parse rows and cells, normalizing spacing and escaped pipes.
4. Serialize to CSV rows.
5. Emit CSV text to stdout.

## Error States

- **NoTableFound**: No valid Markdown table exists in the input.
- **UnreadableInput**: The file cannot be opened or input stream cannot be read.
- **MalformedTable**: A table-like block cannot be parsed into consistent rows/columns.
