"""ASCII-only tokenization and lightweight stemming for citeseek."""

import re

_ASCII_LOWER = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")
_WORDS = re.compile(r"[a-z0-9]+")
_STOP_WORDS = frozenset(
    [
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "for",
        "from",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "that",
        "the",
        "to",
        "with",
    ]
)


def stem(word):
    """Apply the first matching suffix rule once to an already filtered word."""
    if len(word) > 4 and word.endswith("ies"):
        return word[:-3] + "y"
    if len(word) > 5 and word.endswith("ing"):
        return word[:-3]
    if len(word) > 4 and word.endswith("ed"):
        return word[:-2]
    if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):
        return word[:-1]
    return word


def tokens(text):
    """Return filtered, stemmed ASCII alphanumeric words in input order."""
    lowered = text.translate(_ASCII_LOWER)
    return [
        stem(word) for word in _WORDS.findall(lowered) if len(word) > 1 and word not in _STOP_WORDS
    ]
