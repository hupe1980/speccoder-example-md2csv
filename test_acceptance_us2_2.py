# Scenarios: US2-2
# Given a file that contains no Markdown table, when the user invokes the CLI, then the tool reports that no table was found.

import subprocess
from pathlib import Path


def test_file_with_no_markdown_table_reports_no_table_found(tmp_path: Path) -> None:
    md_file = tmp_path / "notes.md"
    md_file.write_text("# Notes\n\nThis document has no tables.\n", encoding="utf-8")

    result = subprocess.run(
        ["md2csv", str(md_file)],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode != 0
    assert "no table was found" in result.stderr.lower()