"""md2csv package."""

from __future__ import annotations

from argparse import ArgumentParser, Namespace
from pathlib import Path
import sys
from typing import Sequence


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(prog="md2csv", description="Convert Markdown tables to CSV.")
    parser.add_argument("file", nargs="?", type=Path, help="Markdown file to read; defaults to stdin")
    return parser


def run(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return 0


def main(argv: Sequence[str] | None = None) -> None:
    raise SystemExit(run(argv))
