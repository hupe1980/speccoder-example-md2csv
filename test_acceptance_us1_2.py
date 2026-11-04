import subprocess
import sys


def test_us1_2_preserves_header_order_and_row_order():
    markdown = (
        "| first | second | third |\n"
        "| --- | --- | --- |\n"
        "| 1 | 2 | 3 |\n"
        "| 4 | 5 | 6 |\n"
    )

    result = subprocess.run(
        ["md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0
    assert result.stdout == "first,second,third\n1,2,3\n4,5,6\n"
    assert result.stderr == ""
