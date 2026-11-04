import subprocess
import sys


def test_us1_1_valid_markdown_table_on_stdin_outputs_equivalent_csv():
    markdown = (
        "| name | age |\n"
        "| --- | --- |\n"
        "| Alice | 30 |\n"
        "| Bob | 25 |\n"
    )

    result = subprocess.run(
        ["md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "name,age\nAlice,30\nBob,25\n"
    assert result.stderr == ""
