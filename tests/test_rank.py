from harness import row, rows_test

# fmt: off
ROWS = [
    row(["search", "cat", "a.txt", "b.txt", "c.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  0.653  a.txt:1-1\n  the cat sat on the mat\n2  0.516  b.txt:1-2\n  dogs chase the cat\n2 of 2 chunks shown\n"),
    row(["search", "dog", "a.txt", "b.txt", "c.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  2.132  b.txt:1-2\n  dogs chase the cat\n1 of 1 chunk shown\n"),
    row(["search", "cat dog", "a.txt", "b.txt", "c.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  2.647  b.txt:1-2\n  dogs chase the cat\n2  0.653  a.txt:1-1\n  the cat sat on the mat\n2 of 2 chunks shown\n"),
    row(["search", "cat dog cat", "a.txt", "b.txt", "c.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  2.647  b.txt:1-2\n  dogs chase the cat\n2  0.653  a.txt:1-1\n  the cat sat on the mat\n2 of 2 chunks shown\n"),
    row(["search", "bird", "c.txt", "a.txt", "b.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  1.815  c.txt:1-1\n  birds sing songs\n1 of 1 chunk shown\n"),
    row(["search", "zebra", "a.txt", "b.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "no matches\nexit 1\n"),
    row(["search", "--top", "1", "cat", "a.txt", "b.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  0.225  a.txt:1-1\n  the cat sat on the mat\n1 of 2 chunks shown\n"),
    row(["search", "--top", "2", "cat", "a.txt", "b.txt", "c.txt"], {"a.txt": "the cat sat on the mat\n", "b.txt": "dogs chase the cat\nthe dog barks\n", "c.txt": "birds sing songs\n"}, "1  0.653  a.txt:1-1\n  the cat sat on the mat\n2  0.516  b.txt:1-2\n  dogs chase the cat\n2 of 2 chunks shown\n"),
    row(["search", "cat", "a.txt", "a2.txt"], {"a.txt": "cat\n", "a2.txt": "cat\n"}, "1  0.200  a.txt:1-1\n  cat\n2  0.200  a2.txt:1-1\n  cat\n2 of 2 chunks shown\n"),
    row(["search", "cat", "a2.txt", "a.txt"], {"a.txt": "cat\n", "a2.txt": "cat\n"}, "1  0.200  a2.txt:1-1\n  cat\n2  0.200  a.txt:1-1\n  cat\n2 of 2 chunks shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "alpha alpha alpha alpha alpha beta\n"}, "1  0.641  a.txt:1-1\n  alpha alpha alpha alpha alpha beta\n1 of 1 chunk shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "alpha\nbeta\nbeta\nbeta\nbeta\nbeta\nbeta\n"}, "1  1.000  a.txt:1-4\n  alpha\n1 of 1 chunk shown\n"),
    row(["search", "--lines", "2", "--overlap", "0", "alpha", "a.txt"], {"a.txt": "alpha\nbeta\nalpha alpha\ngamma\n"}, "1  0.268  a.txt:3-4\n  alpha alpha\n2  0.220  a.txt:1-2\n  alpha\n2 of 2 chunks shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx   \n"}, "no matches\nexit 1\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "alpha xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"}, "1  0.333  a.txt:1-1\n  alpha xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n1 of 1 chunk shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "alpha xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n"}, "1  0.333  a.txt:1-1\n  alpha xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx...\n1 of 1 chunk shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "\n\t\n  alpha beta  \nsecond\n"}, "1  0.333  a.txt:1-4\n  alpha beta\n1 of 1 chunk shown\n"),
    row(["search", "alpha", "a.txt"], {"a.txt": "alpha\nalpha\nalpha\n"}, "1  0.556  a.txt:1-3\n  alpha\n1 of 1 chunk shown\n"),
    row(["search", "alpha beta", "a.txt", "b.txt"], {"a.txt": "alpha\nbeta\n", "b.txt": "alpha beta\n"}, "1  0.400  a.txt:1-2\n  alpha\n2  0.400  b.txt:1-1\n  alpha beta\n2 of 2 chunks shown\n"),
    row(["search", "kappa", "a.txt", "b.txt", "c.txt", "d.txt"], {"a.txt": "kappa\n", "b.txt": "kappa kappa\n", "c.txt": "omega\n", "d.txt": "kappa omega\n"}, "1  0.553  b.txt:1-1\n  kappa kappa\n2  0.504  a.txt:1-1\n  kappa\n3  0.373  d.txt:1-1\n  kappa omega\n3 of 3 chunks shown\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
