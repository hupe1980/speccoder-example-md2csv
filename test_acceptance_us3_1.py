import subprocess
import sys


def test_us3_1_trims_spacing_and_preserves_values():
    # US3-1: Given a table with uneven spacing around cell values,
    # When the user converts it,
    # Then the output trims formatting noise and preserves the intended cell values.
    markdown = (
        "|  Name   |   Age  |\n"
        "| ------- | ------ |\n"
        "|  Alice  |   30   |\n"
        "|   Bob   |   25   |\n"
    )

    result = subprocess.run(
        [sys.executable, "-m", "md2csv"],
        input=markdown,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "Name,Age\nAlice,30\nBob,25\n"
