"""Module entry point for md2csv."""

from __future__ import annotations

import sys

from . import main
from .errors import Md2CsvError, exit_code_for_error


if __name__ == "__main__":
    try:
        main()
    except Md2CsvError as error:
        print(error, file=sys.stderr)
        raise SystemExit(exit_code_for_error(error)) from error
