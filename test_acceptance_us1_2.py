import subprocess
import sys
from textwrap import dedent


def test_headers_and_multiple_rows_preserve_order():
    markdown = dedent(
        """\
        | first | second | third |
        | --- | --- | --- |
        | 1 | 2 | 3 |
        | 4 | 5 | 6 |
        """
    )

    result = subprocess.run(
        [sys.executable, "-m", "md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0
    assert result.stdout == "first,second,third\r\n1,2,3\r\n4,5,6\r\n"
    assert result.stderr == ""