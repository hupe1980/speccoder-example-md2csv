"""Shared error types and exit handling for md2csv."""

from __future__ import annotations

from dataclasses import dataclass
import sys


@dataclass(frozen=True)
class Md2CsvError(Exception):
    """Base class for user-facing md2csv errors."""

    message: str
    exit_code: int = 2

    def __str__(self) -> str:
        return self.message


class InputError(Md2CsvError):
    """Raised when input cannot be read or parsed as Markdown table content."""


def exit_code_for_error(error: BaseException) -> int:
    if isinstance(error, Md2CsvError):
        print(error, file=sys.stderr)
        return error.exit_code
    return 1
