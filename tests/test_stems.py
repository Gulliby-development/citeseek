from harness import row, rows_test

# fmt: off
ROWS = [
    row(["search", "story", "a.txt"], {"a.txt": "stories\n"}, "1  0.333  a.txt:1-1\n  stories\n1 of 1 chunk shown\n"),
    row(["search", "stories", "a.txt"], {"a.txt": "story\n"}, "1  0.333  a.txt:1-1\n  story\n1 of 1 chunk shown\n"),
    row(["search", "ties", "a.txt"], {"a.txt": "tie\n"}, "1  0.333  a.txt:1-1\n  tie\n1 of 1 chunk shown\n"),
    row(["search", "pies", "a.txt"], {"a.txt": "pie\n"}, "1  0.333  a.txt:1-1\n  pie\n1 of 1 chunk shown\n"),
    row(["search", "index", "a.txt"], {"a.txt": "indexed\n"}, "1  0.333  a.txt:1-1\n  indexed\n1 of 1 chunk shown\n"),
    row(["search", "indexed", "a.txt"], {"a.txt": "indexes\n"}, "no matches\nexit 1\n"),
    row(["search", "search", "a.txt"], {"a.txt": "searching\n"}, "1  0.333  a.txt:1-1\n  searching\n1 of 1 chunk shown\n"),
    row(["search", "sing", "a.txt"], {"a.txt": "singing\n"}, "1  0.333  a.txt:1-1\n  singing\n1 of 1 chunk shown\n"),
    row(["search", "sing", "a.txt"], {"a.txt": "sing\n"}, "1  0.333  a.txt:1-1\n  sing\n1 of 1 chunk shown\n"),
    row(["search", "king", "a.txt"], {"a.txt": "kings\n"}, "1  0.333  a.txt:1-1\n  kings\n1 of 1 chunk shown\n"),
    row(["search", "bus", "a.txt"], {"a.txt": "buses\n"}, "no matches\nexit 1\n"),
    row(["search", "buse", "a.txt"], {"a.txt": "buses\n"}, "1  0.333  a.txt:1-1\n  buses\n1 of 1 chunk shown\n"),
    row(["search", "class", "a.txt"], {"a.txt": "classs\n"}, "no matches\nexit 1\n"),
    row(["search", "glass", "a.txt"], {"a.txt": "glasss\n"}, "no matches\nexit 1\n"),
    row(["search", "tried", "a.txt"], {"a.txt": "tri\n"}, "1  0.333  a.txt:1-1\n  tri\n1 of 1 chunk shown\n"),
    row(["search", "bed", "a.txt"], {"a.txt": "bed\n"}, "1  0.333  a.txt:1-1\n  bed\n1 of 1 chunk shown\n"),
    row(["search", "red", "a.txt"], {"a.txt": "re\n"}, "no matches\nexit 1\n"),
    row(["search", "cats", "a.txt"], {"a.txt": "cat\n"}, "1  0.333  a.txt:1-1\n  cat\n1 of 1 chunk shown\n"),
    row(["search", "this", "a.txt"], {"a.txt": "this\n"}, "1  0.333  a.txt:1-1\n  this\n1 of 1 chunk shown\n"),
    row(["search", "ss", "a.txt"], {"a.txt": "ss\n"}, "1  0.333  a.txt:1-1\n  ss\n1 of 1 chunk shown\n"),
    row(["search", "yes", "a.txt"], {"a.txt": "ye\n"}, "no matches\nexit 1\n"),
    row(["search", "2024", "a.txt"], {"a.txt": "2024s\n"}, "1  0.333  a.txt:1-1\n  2024s\n1 of 1 chunk shown\n"),
    row(["search", "CAT", "a.txt"], {"a.txt": "cat\n"}, "1  0.333  a.txt:1-1\n  cat\n1 of 1 chunk shown\n"),
    row(["search", "caf\u00e9", "a.txt"], {"a.txt": "caf\n"}, "1  0.333  a.txt:1-1\n  caf\n1 of 1 chunk shown\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
