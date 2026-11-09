"""Line-window construction with citations for citeseek."""

from dataclasses import dataclass

from citeseek.text import tokens


@dataclass
class Chunk:
    """A token-bearing window of a displayed file."""

    file: str
    start: int
    end: int
    words: list[str]
    first_line: str


def _lines(text):
    """Split on LF only, removing CR only when it immediately precedes LF."""
    text = text.removeprefix("\ufeff")

    pieces = text.split("\n")
    has_final_lf = text.endswith("\n")
    if has_final_lf:
        pieces.pop()

    lines = []
    for index, piece in enumerate(pieces):
        if (has_final_lf or index < len(pieces) - 1) and piece.endswith("\r"):
            piece = piece[:-1]
        lines.append(piece)
    return lines


def chunks_of(display, text, size, overlap):
    """Return ordered nonempty line windows with one-based inclusive citations."""
    lines = _lines(text)
    chunks = []
    step = size - overlap
    previous_end = None

    for start in range(1, len(lines) + 1, step):
        end = min(start + size - 1, len(lines))
        if end == previous_end:
            continue
        previous_end = end

        window = lines[start - 1 : end]
        words = [word for line in window for word in tokens(line)]
        if not words:
            continue

        first_line = next(line.strip(" \t") for line in window if line.strip(" \t"))
        chunks.append(Chunk(display, start, end, words, first_line))

    return chunks
