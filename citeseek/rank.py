"""Exact corpus scoring and decimal formatting for citeseek."""

from fractions import Fraction


def score_all(chunks, query_words):
    """Return exact BM25-style scores aligned with the input chunks."""
    if not chunks:
        return []

    query = set(query_words)
    frequencies = []
    lengths = []
    document_frequency = {}
    total_words = 0

    for chunk in chunks:
        counts = {}
        for word in chunk.words:
            counts[word] = counts.get(word, 0) + 1
        frequencies.append(counts)
        lengths.append(len(chunk.words))
        total_words += len(chunk.words)
        for word in counts:
            document_frequency[word] = document_frequency.get(word, 0) + 1

    count = len(chunks)
    average_length = Fraction(total_words, count)
    scores = []
    for counts, length in zip(frequencies, lengths):
        score = Fraction(0)
        for term in query:
            term_frequency = counts.get(term, 0)
            if not term_frequency:
                continue
            doc_frequency = document_frequency[term]
            inverse_frequency = Fraction(2 * count - 2 * doc_frequency + 1, 2 * doc_frequency + 1)
            normalization = Fraction(3, 2) * (
                Fraction(1, 4) + Fraction(3 * length, 4) / average_length
            )
            score += (
                inverse_frequency
                * term_frequency
                * Fraction(5, 2)
                / (term_frequency + normalization)
            )
        scores.append(score)
    return scores


def fixed3(score):
    """Format a nonnegative score to three decimals with exact half-up rounding."""
    scaled_numerator = score.numerator * 1000
    quotient, remainder = divmod(scaled_numerator, score.denominator)
    if 2 * remainder >= score.denominator:
        quotient += 1
    whole, fractional = divmod(quotient, 1000)
    return f"{whole}.{fractional:03d}"
