import subprocess
import sys
from textwrap import dedent


def test_valid_markdown_table_on_stdin_outputs_equivalent_csv():
    markdown = dedent(
        """\
        | name | age |
        | --- | --- |
        | Alice | 30 |
        | Bob | 31 |
        """
    )

    result = subprocess.run(
        [sys.executable, "-m", "md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert result.stdout == "name,age\r\nAlice,30\r\nBob,31\r\n"
    assert result.stderr == ""