# Scenarios: US2-1
# Given a readable Markdown file, when the user invokes the CLI with that file, then the tool outputs CSV for the table content it finds.

import subprocess
from pathlib import Path


def test_readable_markdown_file_outputs_csv(tmp_path: Path) -> None:
    md_file = tmp_path / "table.md"
    md_file.write_text(
        "| Name | Value |\n| --- | --- |\n| Alpha | 1 |\n",
        encoding="utf-8",
    )

    result = subprocess.run(
        ["md2csv", str(md_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "Name,Value\nAlpha,1\n"
    assert result.stderr == ""