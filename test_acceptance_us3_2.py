from __future__ import annotations

import importlib

import pytest


SCENARIO_IDS = ["US3-2"]


def test_acceptance_us3_2_empty_cells_and_escaped_pipe():
    md2csv = importlib.import_module("md2csv")

    input_markdown = (
        "| Name | Note | Value |\n"
        "| --- | --- | --- |\n"
        "| Alpha | | 1 |\n"
        "| Beta | A \\| B | |\n"
    )

    result = md2csv.run([input_markdown])

    assert result == 0
