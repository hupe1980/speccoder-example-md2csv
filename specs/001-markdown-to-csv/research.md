# Research Notes

## 1) Markdown table parsing approach
- **Decision**: Use a small, deterministic parser for GitHub-flavored pipe tables and select the first valid table in the input.
- **Rationale**: The feature spec emphasizes standard Markdown tables, order preservation, and clear errors. A focused parser keeps behavior predictable and avoids pulling in a heavy dependency for a narrow CLI utility.
- **Alternatives considered**:
  - Full Markdown parser: broader syntax support, but more complexity and less control over table extraction behavior.
  - Regex-only parsing: simpler, but brittle for escaped pipes and CSV escaping edge cases.

## 2) Input handling
- **Decision**: Support stdin when no file argument is provided, and file path input when present; treat unreadable files as user-facing errors.
- **Rationale**: This matches the user stories and allows both interactive and scripted use.
- **Alternatives considered**:
  - Require only file input: simpler, but fails the core stdin requirement.
  - Require only stdin: reduces flexibility and fails the file workflow.

## 3) CSV emission
- **Decision**: Use Python's built-in `csv` module to generate output.
- **Rationale**: It guarantees CSV-compliant quoting and escaping for commas, quotes, and line breaks while minimizing custom serialization logic.
- **Alternatives considered**:
  - Manual CSV serialization: possible, but easy to get escaping wrong.
  - Third-party CSV writer: unnecessary given the standard library support.

## 4) Error reporting
- **Decision**: Emit clear, human-readable error messages to stderr and use non-zero exit codes for invalid input, unreadable files, or missing tables.
- **Rationale**: The spec requires clear messages and user-facing errors for invalid inputs.
- **Alternatives considered**:
  - Silent no-op on empty/no-table input: rejected because it would hide failures.
  - Structured JSON errors: unnecessary for the initial CLI scope.

## 5) CLI contract shape
- **Decision**: Define a minimal CLI contract with one optional positional file argument and standard output for CSV.
- **Rationale**: Keeps the tool simple and aligned with the current project being a command-line utility.
- **Alternatives considered**:
  - Multiple flags for table selection and output options: not required by the spec and would increase surface area.
  - Interactive prompts: incompatible with piping and scripting.
