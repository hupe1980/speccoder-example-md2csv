"""md2csv package."""

from __future__ import annotations

from argparse import ArgumentParser
from pathlib import Path
from typing import Sequence

from .errors import Md2CsvError, exit_code_for_error


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="md2csv", description="Convert Markdown tables to CSV.")
    parser.add_argument("file", nargs="?", type=Path, help="Markdown file to read; defaults to stdin")
    return parser


def run(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return 0


def main(argv: Sequence[str] | None = None) -> None:
    try:
        raise SystemExit(run(argv))
    except Md2CsvError as error:
        raise SystemExit(exit_code_for_error(error)) from error

