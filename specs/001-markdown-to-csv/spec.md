# Feature Specification: Markdown to CSV CLI

**Feature Branch**: `[001-markdown-to-csv]`  
**Created**: 2026-11-03  
**Status**: Draft  
**Input**: User description: "a CLI that turns Markdown tables into CSV"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Convert a table from standard input (Priority: P1)

A user provides Markdown table text through standard input and receives CSV output for the same table.

**Why this priority**: This is the core value of the tool and the main reason users would use it.

**Independent Test**: Can be fully tested by piping a Markdown table into the CLI and verifying the CSV output matches the input table data.

**Acceptance Scenarios**:

1. **Given** a valid Markdown table on standard input, **When** the user runs the CLI without file arguments, **Then** the tool outputs equivalent CSV rows and columns.
2. **Given** a Markdown table with headers and multiple rows, **When** the user runs the CLI, **Then** the output preserves header order and row order.

---

### User Story 2 - Convert a table from a file (Priority: P2)

A user provides a file containing one or more Markdown tables and receives CSV output for the selected table or tables.

**Why this priority**: File-based input is a common workflow for saved documentation and scripted use.

**Independent Test**: Can be fully tested by running the CLI against a sample Markdown file and checking that the expected CSV is produced.

**Acceptance Scenarios**:

1. **Given** a readable Markdown file, **When** the user invokes the CLI with that file, **Then** the tool outputs CSV for the table content it finds.
2. **Given** a file that contains no Markdown table, **When** the user invokes the CLI, **Then** the tool reports that no table was found.

---

### User Story 3 - Handle common table formatting issues (Priority: P3)

A user provides Markdown tables that include extra spacing, empty cells, or escaped pipe characters and still gets usable CSV output.

**Why this priority**: Real-world Markdown often contains minor formatting variation, and the tool should remain useful on imperfect input.

**Independent Test**: Can be fully tested with sample tables covering spacing and escaping edge cases.

**Acceptance Scenarios**:

1. **Given** a table with uneven spacing around cell values, **When** the user converts it, **Then** the output trims formatting noise and preserves the intended cell values.
2. **Given** a table containing empty cells or escaped pipe characters, **When** the user converts it, **Then** the output keeps the correct column count and cell content.

---

### Edge Cases

- Input contains multiple Markdown tables and the user needs one table selected deterministically.
- Input contains table-like text that is not a valid Markdown table.
- Table cells contain commas, quotes, or newlines that require CSV-safe escaping.
- The input table has inconsistent row lengths or missing separator rows.
- The input file or stream is empty.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The tool MUST accept Markdown table content from standard input.
- **FR-002**: The tool MUST accept Markdown table content from a file path provided by the user.
- **FR-003**: The tool MUST convert each Markdown table row into a corresponding CSV row.
- **FR-004**: The tool MUST preserve the order of columns and rows from the source table.
- **FR-005**: The tool MUST preserve header rows when they are present in the Markdown input.
- **FR-006**: The tool MUST produce CSV-compliant escaping for commas, quotes, and line breaks inside cell values.
- **FR-007**: The tool MUST treat empty table cells as empty CSV fields.
- **FR-008**: The tool MUST ignore Markdown formatting characters that are not part of the cell content.
- **FR-009**: The tool MUST report a clear message when no valid Markdown table is found in the input.
- **FR-010**: The tool MUST report a clear message when the input cannot be read or parsed as a table.

### Key Entities *(include if feature involves data)*

- **Markdown Table**: A structured set of header and body rows represented in Markdown text, including cell values and separators.
- **CSV Output**: A comma-separated text representation of the same tabular data, including escaped values where needed.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can convert a valid Markdown table to CSV in a single command with no manual cleanup for at least 95% of typical documentation tables.
- **SC-002**: At least 90% of first-time users can successfully convert a sample table without consulting additional instructions.
- **SC-003**: For valid input, the tool preserves all table rows and columns exactly as presented in the source table structure.
- **SC-004**: When the input contains no valid table, users receive a clear error message in all tested cases.

## Assumptions

- The primary audience is users who work with documentation, notes, or generated Markdown.
- The initial version focuses on converting one chosen table per input unless multiple-table behavior is later clarified.
- The tool is expected to follow standard CSV conventions for quoting and escaping.
- Empty input and invalid table structure are treated as user-facing errors rather than silent no-ops.
