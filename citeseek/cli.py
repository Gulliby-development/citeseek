"""Command parsing, input validation and chunks output for citeseek."""

from citeseek.chunks import chunks_of
from citeseek.rank import fixed3, score_all
from citeseek.text import tokens

_USAGE = (
    "usage: citeseek chunks [--lines N] [--overlap M] FILE...\n"
    "       citeseek search [--lines N] [--overlap M] [--top K] QUERY FILE...\n"
)
_OPTION_RANGES = {
    "--lines": (1, 100),
    "--overlap": (0, 99),
    "--top": (1, 50),
}


def _error(stderr, message):
    stderr.write(f"citeseek: {message}\n")
    return 2


def _number(value, low, high):
    """Parse bounded ASCII decimal syntax without converting huge invalid values."""
    if not value or any(char < "0" or char > "9" for char in value):
        return None
    if len(value) > 1 and value[0] == "0":
        return None
    spelling = str(high)
    if len(value) > len(spelling) or (len(value) == len(spelling) and value > spelling):
        return None
    number = int(value)
    return number if number >= low else None


def main(argv, stdout, stderr):
    """Run one citeseek command using only the supplied output streams."""
    if argv == ["--help"]:
        stdout.write(_USAGE)
        return 0
    if not argv:
        return _error(stderr, "missing command (chunks or search)")
    command = argv[0]
    if command not in ("chunks", "search"):
        return _error(stderr, f'unknown command "{command}"')

    values = {"--lines": 4, "--overlap": 1, "--top": 3}
    positionals = []
    index = 1
    while index < len(argv):
        argument = argv[index]
        option = argument.split("=", 1)[0]
        if option in _OPTION_RANGES and (option != "--top" or command == "search"):
            if "=" in argument:
                value = argument.split("=", 1)[1]
                index += 1
            elif index + 1 >= len(argv):
                return _error(stderr, f"{option} needs a value")
            else:
                value = argv[index + 1]
                index += 2
            low, high = _OPTION_RANGES[option]
            parsed = _number(value, low, high)
            if parsed is None:
                return _error(
                    stderr,
                    f'invalid {option} "{value}" (expected a whole number from {low} to {high})',
                )
            values[option] = parsed
            continue
        if argument.startswith("-"):
            return _error(stderr, f'unknown option "{option}"')
        positionals.append(argument)
        index += 1

    lines, overlap, top = values["--lines"], values["--overlap"], values["--top"]
    if overlap >= lines:
        return _error(stderr, "--overlap must be less than --lines")
    if command == "search":
        if not positionals:
            return _error(stderr, "missing QUERY")
        query = positionals.pop(0)
    if not positionals:
        return _error(stderr, "missing FILE")

    chunks = []
    seen = set()
    for name in positionals:
        display = name.replace("\\", "/")
        if name in seen:
            return _error(stderr, f'duplicate file "{display}"')
        seen.add(name)
        try:
            with open(name, "rb") as handle:
                content = handle.read()
        except OSError:
            return _error(stderr, f"{display}: cannot read the file")
        try:
            text = content.decode("utf-8", errors="strict")
        except UnicodeDecodeError:
            return _error(stderr, f"{display}: input is not valid UTF-8")
        chunks.extend(chunks_of(display, text, lines, overlap))

    if command == "chunks":
        for chunk in chunks:
            stdout.write(f"{chunk.file}:{chunk.start}-{chunk.end}  {len(chunk.words)}\n")
        count = len(chunks)
        stdout.write(
            f"{count} {'chunk' if count == 1 else 'chunks'} from "
            f"{len(positionals)} {'file' if len(positionals) == 1 else 'files'}\n"
        )
        return 0

    query_words = tokens(query)
    if not query_words:
        return _error(stderr, "query has no searchable words")
    if not chunks:
        return _error(stderr, "no searchable text")

    scores = score_all(chunks, query_words)
    matches = [(chunk, score) for chunk, score in zip(chunks, scores) if score > 0]
    matches.sort(key=lambda match: match[1], reverse=True)
    total = len(matches)
    if not matches:
        stdout.write("no matches\n")
        return 1

    selected = matches[:top]
    for rank, (chunk, score) in enumerate(selected, 1):
        snippet = chunk.first_line
        if len(snippet) > 60:
            snippet = snippet[:57] + "..."
        stdout.write(
            f"{rank}  {fixed3(score)}  {chunk.file}:{chunk.start}-{chunk.end}\n  {snippet}\n"
        )
    stdout.write(f"{len(selected)} of {total} {'chunk' if total == 1 else 'chunks'} shown\n")
    return 0
