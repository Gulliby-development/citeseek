from harness import row, rows_test

# fmt: off
ROWS = [
    row(["chunks", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\n"}, "a.txt:1-4  4\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\nfive\n"}, "a.txt:1-4  4\na.txt:4-5  2\n2 chunks from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\nfive\nsix\nseven\n"}, "a.txt:1-4  4\na.txt:4-7  4\n2 chunks from 1 file\n"),
    row(["chunks", "--lines", "2", "--overlap", "0", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\nfive\n"}, "a.txt:1-2  2\na.txt:3-4  2\na.txt:5-5  1\n3 chunks from 1 file\n"),
    row(["chunks", "--lines", "2", "--overlap", "1", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\n"}, "a.txt:1-2  2\na.txt:2-3  2\na.txt:3-4  2\n3 chunks from 1 file\n"),
    row(["chunks", "--lines", "3", "--overlap", "2", "a.txt"], {"a.txt": "one\ntwo\nthree\nfour\nfive\n"}, "a.txt:1-3  3\na.txt:2-4  3\na.txt:3-5  3\n3 chunks from 1 file\n"),
    row(["chunks", "--lines", "1", "--overlap", "0", "a.txt"], {"a.txt": "one\n\nthree\n"}, "a.txt:1-1  1\na.txt:3-3  1\n2 chunks from 1 file\n"),
    row(["chunks", "--lines", "2", "--overlap", "0", "a.txt"], {"a.txt": "\n\none\ntwo\n\n\n"}, "a.txt:3-4  2\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "one\r\ntwo\r\nthree\r\n"}, "a.txt:1-3  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "one two\nthree"}, "a.txt:1-2  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "\ufeffone\ntwo\n"}, "a.txt:1-2  2\n1 chunk from 1 file\n"),
    row(["chunks", "--lines", "5", "--overlap", "0", "a.txt"], {"a.txt": "one\n\n\n\n\n"}, "a.txt:1-5  1\n1 chunk from 1 file\n"),
    row(["chunks", "--lines=2", "--overlap=0", "a.txt", "b.txt"], {"a.txt": "one\ntwo\nthree\n", "b.txt": "four\n"}, "a.txt:1-2  2\na.txt:3-3  1\nb.txt:1-1  1\n3 chunks from 2 files\n"),
    row(["chunks", "b.txt", "a.txt"], {"a.txt": "one\n", "b.txt": "two\nthree\n"}, "b.txt:1-2  2\na.txt:1-1  1\n2 chunks from 2 files\n"),
    row(["chunks", "a.txt"], {"a.txt": "\n"}, "0 chunks from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": ""}, "0 chunks from 1 file\n"),
    row(["chunks", "--lines", "100", "--overlap", "0", "a.txt"], {"a.txt": "one\ntwo\n"}, "a.txt:1-2  2\n1 chunk from 1 file\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
