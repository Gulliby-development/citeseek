from harness import row, rows_test

# fmt: off
ROWS = [
    row(["chunks", "a.txt"], {"a.txt": "the cat sat on the mat\n"}, "a.txt:1-1  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "A a I x 7 42\n"}, "a.txt:1-1  1\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "Hello, World! hello-world hello_world\n"}, "a.txt:1-1  6\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "caf\u00e9 na\u00efve \u212a K k\n"}, "a.txt:1-1  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "x\u00b2 ab\u00df cd\u0130 ef\n"}, "a.txt:1-1  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "and the of in is it to with\n"}, "0 chunks from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "AND The OF\n"}, "0 chunks from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "2024-05-01 v1.2.3\n"}, "a.txt:1-1  4\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "\ufeffalpha beta\n"}, "a.txt:1-1  2\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "alpha\tbeta\u3000gamma\n"}, "a.txt:1-1  3\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "a1 b2 1a 22\n"}, "a.txt:1-1  4\n1 chunk from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "\n\n\n"}, "0 chunks from 1 file\n"),
    row(["chunks", "a.txt"], {"a.txt": "--- ... ___\n"}, "0 chunks from 1 file\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
