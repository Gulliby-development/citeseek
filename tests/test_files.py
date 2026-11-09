from harness import row, rows_test

# fmt: off
ROWS = [
    row(["chunks", "nope.txt"], {}, "! citeseek: nope.txt: cannot read the file\nexit 2\n"),
    row(["chunks", "a.txt", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: duplicate file \"a.txt\"\nexit 2\n"),
    row(["search", "cat", "a.txt", "missing.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: missing.txt: cannot read the file\nexit 2\n"),
    row(["search", "cat", "empty.txt"], {"empty.txt": "\n\n"}, "! citeseek: no searchable text\nexit 2\n"),
    row(["search", "the of", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: query has no searchable words\nexit 2\n"),
    row(["search", "", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: query has no searchable words\nexit 2\n"),
    row(["search", "\u212a", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: query has no searchable words\nexit 2\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
