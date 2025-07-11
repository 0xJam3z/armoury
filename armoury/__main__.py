"""
Main entry point for running Armoury as a module.
"""
import sys

if sys.version_info < (3, 6):
    raise SystemExit(
        "Sorry, Python 3.6 (or greater) is required to run Armoury. ABORTING."
    )

from .app import main

if __name__ == "__main__":
    main()
