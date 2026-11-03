"""CSV emission helpers for md2csv."""

from __future__ import annotations

import csv
import io

from .parser import MarkdownTable


def markdown_table_to_csv(table: MarkdownTable) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(table.header_cells)
    writer.writerows(table.body_rows)
    return buffer.getvalue()
