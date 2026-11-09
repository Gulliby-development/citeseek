from harness import row, rows_test

# fmt: off
ROWS = [
    row([], {}, "! citeseek: missing command (chunks or search)\nexit 2\n"),
    row(["bogus"], {}, "! citeseek: unknown command \"bogus\"\nexit 2\n"),
    row(["--help"], {}, "usage: citeseek chunks [--lines N] [--overlap M] FILE...\n       citeseek search [--lines N] [--overlap M] [--top K] QUERY FILE...\n"),
    row(["--help", "chunks"], {}, "! citeseek: unknown command \"--help\"\nexit 2\n"),
    row(["chunks"], {}, "! citeseek: missing FILE\nexit 2\n"),
    row(["search"], {}, "! citeseek: missing QUERY\nexit 2\n"),
    row(["search", "cat"], {}, "! citeseek: missing FILE\nexit 2\n"),
    row(["chunks", "--top", "2", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: unknown option \"--top\"\nexit 2\n"),
    row(["chunks", "--top=2", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: unknown option \"--top\"\nexit 2\n"),
    row(["search", "--top"], {}, "! citeseek: --top needs a value\nexit 2\n"),
    row(["chunks", "-x", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: unknown option \"-x\"\nexit 2\n"),
    row(["search", "--lines=", "cat", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --lines \"\" (expected a whole number from 1 to 100)\nexit 2\n"),
    row(["chunks", "--lines", "0", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --lines \"0\" (expected a whole number from 1 to 100)\nexit 2\n"),
    row(["chunks", "--lines", "101", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --lines \"101\" (expected a whole number from 1 to 100)\nexit 2\n"),
    row(["chunks", "--overlap", "100", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --overlap \"100\" (expected a whole number from 0 to 99)\nexit 2\n"),
    row(["chunks", "--lines", "03", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --lines \"03\" (expected a whole number from 1 to 100)\nexit 2\n"),
    row(["chunks", "--lines", "4", "--overlap", "4", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: --overlap must be less than --lines\nexit 2\n"),
    row(["chunks", "--lines", "1", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: --overlap must be less than --lines\nexit 2\n"),
    row(["search", "--top", "51", "cat", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --top \"51\" (expected a whole number from 1 to 50)\nexit 2\n"),
    row(["search", "--top", "0", "cat", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "! citeseek: invalid --top \"0\" (expected a whole number from 1 to 50)\nexit 2\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
