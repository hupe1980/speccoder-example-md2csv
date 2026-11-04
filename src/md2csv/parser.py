"""Markdown table parsing helpers for md2csv."""

from __future__ import annotations

from dataclasses import dataclass

from .errors import MalformedTableError


@dataclass(frozen=True)
class MarkdownTable:
    header_cells: list[str]
    body_rows: list[list[str]]
    source_index: int
    raw_source: str


class MarkdownTableError(ValueError):
    """Raised when Markdown table input cannot be parsed."""


def _split_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped:
        return []
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    current: list[str] = []
    escape = False
    for ch in stripped:
        if escape:
            current.append(ch)
            escape = False
        elif ch == "\\":
            escape = True
        elif ch == "|":
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    cells.append("".join(current).strip())
    return cells


def parse_markdown_table(text: str) -> MarkdownTable:
    lines = [line for line in text.splitlines() if line.strip()]
    for idx in range(len(lines) - 1):
        header = _split_row(lines[idx])
        separator = _split_row(lines[idx + 1])
        if not header or len(header) != len(separator):
            continue
        if not all(cell and set(cell.replace(":", "")) <= {"-"} for cell in separator):
            continue
        body_rows: list[list[str]] = []
        for line in lines[idx + 2 :]:
            row = _split_row(line)
            if not row:
                break
            if len(row) != len(header):
                raise MalformedTableError("Malformed table row")
            body_rows.append(row)
        if body_rows:
            return MarkdownTable(header, body_rows, idx, "\n".join(lines[idx : idx + 2 + len(body_rows)]))
    raise MarkdownTableError("No valid Markdown table found")
