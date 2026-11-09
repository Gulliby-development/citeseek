"""python -m citeseek: the command line entry point."""

import sys

from citeseek.cli import main

if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    sys.stderr.reconfigure(encoding="utf-8", newline="\n")
    sys.exit(main(sys.argv[1:], sys.stdout, sys.stderr))
