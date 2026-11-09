"""Row tests: every row writes its files into a fresh folder, runs the command line there and compares the text."""

import io

import pytest

from citeseek.cli import main


def row(args, files, expected):
    return (args, files, expected)


def run_row(args, files):
    """Standard output, then every line of standard error as `! LINE`, then `exit N` when the status is not 0."""
    for name, text in files.items():
        with open(name, "wb") as handle:
            handle.write(text.encode("utf-8"))
    out, err = io.StringIO(), io.StringIO()
    code = main(args, out, err)
    result = out.getvalue() + "".join(f"! {line}\n" for line in err.getvalue().splitlines())
    return result + (f"exit {code}\n" if code else "")


def rows_test(rows):
    ids = [f"row{n}" for n in range(1, len(rows) + 1)]

    @pytest.mark.parametrize(("args", "files", "expected"), rows, ids=ids)
    def test_rows(args, files, expected, tmp_path, monkeypatch):
        monkeypatch.chdir(tmp_path)
        assert run_row(args, files) == expected

    return test_rows
