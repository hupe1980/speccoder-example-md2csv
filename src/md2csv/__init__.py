"""Convenience exports for the md2csv package."""

from __future__ import annotations

from .cli import build_parser, main, run
from .csv_writer import markdown_table_to_csv
from .errors import InputError, MalformedTableError, Md2CsvError, exit_code_for_error
from .parser import MarkdownTableError, parse_markdown_table

__all__ = [
    "MarkdownTableError",
    "InputError",
    "MalformedTableError",
    "Md2CsvError",
    "build_parser",
    "exit_code_for_error",
    "main",
    "markdown_table_to_csv",
    "parse_markdown_table",
    "run",
]
