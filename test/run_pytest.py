#!/usr/bin/env python

"""Run automated testing with code coverage.
Produces a report in HTML format, XML format, and text format. The produced report is ready to be
shipped to various tools.
"""

import os
import sys
from pathlib import Path
from shutil import rmtree
from subprocess import CalledProcessError, run


def _main():
    # Execute tests from the root directory
    root = Path(__file__).parent.parent.resolve()
    os.chdir(root)

    # Clean up old coverage reports
    condemned = [
        Path(root, "coverage.txt"),
        Path(root, "coverage.xml"),
        Path(root, "coverage.json"),
        Path(root, "htmlcov"),
    ] + list(Path(root).glob(".coverage*"))
    for c in condemned:
        if c.is_file():
            c.unlink()
        elif c.is_dir():
            rmtree(c)
    run(["coverage", "erase"], check=True)

    # Run only some tests - no output capture (-s)
    try:
        filt = ["-k", sys.argv[1], "-s"]
        xdist = ["-p", "no:xdist"]
    except IndexError:
        filt = []
        xdist = ["-n4"]

    cmd = [
        "pytest",
        "--cov=test",
        "-vvv",
        "-m",
        "not flaky",
        "-n4",
        "--force-sugar",
        "-p",
        "no:cacheprovider",
        "--html=pytest_report/index.html",
        "--durations=10",
        "--dist=loadgroup",
        "test/tests",
    ]

    try:
        print(f"Running: {' '.join(cmd)}")  # noqa
        run(cmd, check=True)
    except CalledProcessError:
        sys.exit(1)

    # Save coverage report as text
    with open("coverage.txt", "wb") as fp:
        run(["coverage", "report"], check=True, stdout=fp)

    # Produce HTML and XML reports too
    for mode in ("html", "xml", "json"):
        run(["coverage", mode], check=True)


if __name__ == "__main__":
    _main()