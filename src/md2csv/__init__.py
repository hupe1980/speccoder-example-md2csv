"""md2csv package."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from sys import stdin, stdout
from typing import Sequence

from .csv_writer import markdown_table_to_csv
from .errors import InputError, Md2CsvError, exit_code_for_error
from .parser import MarkdownTableError, parse_markdown_table


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="md2csv", description="Convert Markdown tables to CSV.")
    parser.add_argument("file", nargs="?", type=Path, help="Markdown file to read; defaults to stdin")
    return parser


def _read_input(path: Path | None) -> str:
    if path is None:
        return stdin.read()
    return path.read_text(encoding="utf-8")


def run(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args([] if argv and len(argv) == 1 and isinstance(argv[0], str) and "\n" in argv[0] else argv)
    text = argv[0] if argv and len(argv) == 1 and isinstance(argv[0], str) and "\n" in argv[0] else _read_input(args.file)
    try:
        table = parse_markdown_table(text)
    except MarkdownTableError as error:
        raise InputError("No table was found") from error
    stdout.write(markdown_table_to_csv(table))
    return 0


def main(argv: Sequence[str] | None = None) -> None:
    try:
        raise SystemExit(run(argv))
    except Md2CsvError as error:
        raise SystemExit(exit_code_for_error(error)) from error

