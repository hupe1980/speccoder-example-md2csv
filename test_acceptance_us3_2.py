import subprocess
import sys


def test_us3_2_keeps_column_count_and_content_with_empty_and_escaped_pipes():
    # US3-2: Given a table containing empty cells or escaped pipe characters,
    # When the user converts it,
    # Then the output keeps the correct column count and cell content.
    markdown = (
        "| Item | Notes | Value |\n"
        "| ---- | ----- | ----- |\n"
        "| Foo  |       | 100   |\n"
        "| Bar  | A \\\| B |       |\n"
    )

    result = subprocess.run(
        [sys.executable, "-m", "md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "Item,Notes,Value\nFoo,,100\nBar,A | B,\n"
