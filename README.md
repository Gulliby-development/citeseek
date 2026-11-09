<p align="center"><img src="docs/logo.svg" width="96" alt="" /></p>

# citeseek

[![CI](https://github.com/Gulliby-development/citeseek/actions/workflows/ci.yml/badge.svg)](https://github.com/Gulliby-development/citeseek/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

citeseek searches local plain-text notes, documentation, and transcripts for useful passages and prints the strongest matches with line citations such as `notes.txt:1-4`. It is intended for prompt authors and agent-tool builders who want a reproducible retrieval step they can inspect and test. It needs no model, embeddings, index, network connection, or key: each invocation searches only the files supplied to it.

citeseek supports Python 3.11 and newer on Windows, macOS, and Linux. The runtime uses only Python's standard library. Results are deterministic: token handling and scoring are defined below, and ranking uses exact fractions rather than floating-point arithmetic. Run it from the repository directory with `python -m citeseek`.

## Setup

For development, create and activate a virtual environment, then install the pinned development tools:

```sh
python -m venv .venv
```

On macOS or Linux, activate it with `source .venv/bin/activate`; in Windows Command Prompt use `.venv\\Scripts\\activate.bat`, or in PowerShell use `.venv\\Scripts\\Activate.ps1`. Then install the development requirements:

```sh
pip install -r requirements-dev.txt
```

These requirements provide pytest and Ruff for development; citeseek itself has no third-party runtime dependencies.

## Text processing

Each input text is processed as follows:

1. Only ASCII capital letters A through Z are lowercased. No Unicode case folding is performed.
2. Maximal runs of ASCII letters `a-z` and digits `0-9` form words. Every other character, including punctuation, whitespace, and non-ASCII characters, separates words.
3. One-character words are discarded.
4. The stop words `an and are as at be by for from in is it of on or that the to with` are discarded. The one-character word `a` is already removed by the preceding rule.
5. Remaining words are stemmed once, using the first applicable rule: words longer than 4 characters ending in `ies` replace that suffix with `y`; otherwise words longer than 5 ending in `ing` lose `ing`; otherwise words longer than 4 ending in `ed` lose `ed`; otherwise words longer than 3 ending in `s` but not `ss` lose the final `s`. No stemming rule is applied a second time, and discarded-word checks are not repeated after stemming.

For example, `stories` becomes `story`, while `buses` becomes `buse`; `glass` is unchanged. Only the specified ASCII characters have special treatment.

## Chunks and citations

Files are decoded as strict UTF-8, with exactly one initial byte order mark (BOM) ignored. Splitting occurs only at LF. A CR immediately before an LF is removed; a CR elsewhere remains part of its line. A trailing empty piece caused by a final LF is not counted as a line, so ending a file with LF does not add a line. Citations use one-based, inclusive line numbers.

The default window is 4 lines with an overlap of 1 line. Windows start at line 1 and advance by `lines - overlap`; each extends up to the configured size or the last available line. A window is suppressed if it ends at the same line as the preceding window, since it adds no new line. Windows containing no searchable words are omitted. For a retained window, all its words are counted in order, and its displayed snippet is the first line in the window that is nonempty after trimming spaces and tabs at both ends.

## Commands

```text
usage: citeseek chunks [--lines N] [--overlap M] FILE...
       citeseek search [--lines N] [--overlap M] [--top K] QUERY FILE...
```

The sole argument `--help` prints this usage and exits successfully. Otherwise the first argument must be `chunks` or `search`. Options can appear among later arguments, take a value as the next argument or in `--option=value` form, and a later occurrence replaces an earlier value:

- `--lines N`: window size, default 4, from 1 through 100.
- `--overlap M`: overlap, default 1, from 0 through 99 and always less than `--lines`.
- `--top K`: maximum search results, default 3, from 1 through 50; it is not accepted by `chunks`.

Values must be unsigned ASCII decimal numbers without leading zeroes (except the valid value `0` for overlap). The search query is the first non-option argument after option parsing; it may be empty or contain spaces. Remaining non-option arguments are file names. The implementation checks arguments from left to right, then checks the overlap relation, missing query, and missing files in that order.

### List chunks

`python -m citeseek chunks [--lines N] [--overlap M] FILE...` prints one line per retained chunk in file and line order:

```text
FILE:FIRST-LAST  WORDS
```

The two spaces before the word count are literal. A final summary reports the number of chunks and files, using singular forms when the count is one (for example, `1 chunk from 1 file`). A file with no retained chunks still counts as a file.

### Search

`python -m citeseek search [--lines N] [--overlap M] [--top K] QUERY FILE...` tokenizes the query using the same rules as file text. Repeated query words count only once.

For the corpus, let `N` be its number of retained chunks, `df(t)` the number of chunks containing term `t`, `tf(t,c)` its frequency in chunk `c`, `len(c)` the number of words in that chunk, and `avg` the total word count divided by `N). With `k1 = 3/2` and `b = 3/4`, each matching query term contributes

```text
idf(t) * tf(t,c) * (k1 + 1) / (tf(t,c) + k1 * (1 - b + b * len(c) / avg))
where idf(t) = (N - df(t) + 1/2) / (df(t) + 1/2)
```

The chunk score is the sum of those contributions. All values are exact `Fraction` calculations. Chunks scoring zero are excluded. Remaining chunks are ordered by exact score from highest to lowest, preserving input chunk order for ties (files follow command-line order, then line order). At most `K` are shown. Scores are rounded to three decimal places with exact half-up rounding. Each result includes its rank, score, citation, and first nonblank snippet; snippets are at most 60 Unicode code points, shortened to the first 57 followed by `...` when longer. A final line reports the shown count and total matches, using `chunk` only when the total is one. If there are no matches, the program prints `no matches` and exits with status 1.

## Errors and exit status

Errors are written to standard error as `citeseek: MESSAGE`; they produce no standard output and exit with status 2. Validation proceeds in this order:

1. Command: no arguments gives `missing command (chunks or search)`; an unrecognized first argument gives `unknown command "X"`.
2. Remaining arguments are inspected left to right. An option at the end without a value gives `--lines needs a value`, `--overlap needs a value`, or `--top needs a value`. Invalid numeric spellings or out-of-range values give `invalid --lines "X" (expected a whole number from 1 to 100)`, `invalid --overlap "X" (expected a whole number from 0 to 99)`, or `invalid --top "X" (expected a whole number from 1 to 50)`. An unrecognized hyphen-prefixed argument gives `unknown option "X"`; for an equals-form option, X is the portion before the equals sign. The chunks command treats `--top` as unknown.
3. After parsing: `--overlap must be less than --lines`, then (for search) `missing QUERY`, then `missing FILE`.
4. Files are read in order. Repeating the same supplied filename gives `duplicate file "X"`; unreadable files give `X: cannot read the file`; invalid UTF-8 gives `X: input is not valid UTF-8`. Duplicate detection uses the literal supplied name. Backslashes in displayed names are rendered as forward slashes.
5. Search-specific checks occur after file reads: `query has no searchable words`, then `no searchable text`. The former applies if the query yields no words; the latter if no file yields any retained chunk.

The exit statuses are 0 for help or successful chunk listing/search, 1 for a valid search with no matches, and 2 for command, option, query, or file errors.

## Examples

The following POSIX shell transcript is shown as supplied:

```text
$ printf 'the cat sat on the mat\nCats chase mice\n\nSearching indexed stories\n' > notes.txt
$ python -m citeseek chunks notes.txt
notes.txt:1-4  9
1 chunk from 1 file
$ python -m citeseek search "cats stories" notes.txt
1  0.810  notes.txt:1-4
  the cat sat on the mat
1 of 1 chunk shown
$ python -m citeseek search --top 0 cats notes.txt 2>&1; echo "exit $?"
citeseek: invalid --top "0" (expected a whole number from 1 to 50)
exit 2
$ python -m citeseek search dogs notes.txt; echo "exit $?"
no matches
exit 1
$ rm notes.txt
```

## Development

The modules are organized around these APIs: `citeseek.text.tokens(text)` and `stem(word)` handle words; `citeseek.chunks.Chunk` and `chunks_of(display, text, size, overlap)` represent and create windows; `citeseek.rank.score_all(chunks, query_words)` returns exact scores and `fixed3(score)` formats them; `citeseek.cli.main(argv, stdout, stderr)` implements the command behavior. The `python -m citeseek` entry point is in `citeseek/__main__.py`.

Install the development requirements as described above, then run all three project checks from the repository directory:

```sh
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
```

See the [MIT License](LICENSE) for license terms.

---

Built with [BAKED](https://github.com/Gulliby-development/baked), an open-source coding agent (bench round R87).
