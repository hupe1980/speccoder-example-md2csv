# Research: Markdown to CSV CLI

## Parser Approach
- Use the existing `md2csv` parsing implementation already established in the package.
- Keep the parser standard-library only so the CLI remains offline-friendly and easy to install.
- Select the first valid Markdown table in the provided input to match the current quickstart and scope assumptions.

## Input Handling
- Support both stdin and an explicit file path.
- Treat empty input as an error condition rather than producing empty CSV.
- Preserve row order and column order exactly as they appear in the source table.

## Markdown Normalization
- Trim formatting noise around cell values, especially outer whitespace and outer pipe characters.
- Preserve escaped pipe characters as literal content within a cell.
- Preserve empty cells so the resulting CSV column count remains stable.

## CSV Emission
- Emit RFC-compliant CSV using the standard library writer.
- Rely on CSV quoting rules to escape commas, quotes, and line breaks.
- Write output directly to stdout for shell-friendly composition.

## Error Handling
- Use clear, user-facing messages for:
  - no valid table found
  - malformed table structure
  - unreadable input
- Exit non-zero for all error conditions.

## Validation
- The quickstart scenarios are sufficient to validate the current user-facing behavior:
  1. stdin conversion
  2. file conversion
  3. no-table handling
  4. escaped pipes and empty cells