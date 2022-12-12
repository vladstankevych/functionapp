import os, sys
from pathlib import Path

from subprocess import run
      
root = Path(".").resolve()

cmd = [
    "pytest",
    "--cov=/home/runner/work/functionapp/functionapp",
    "-vvv",
    "-m not flaky",
    "-n4"
    "--force-sugar",
    "-p",
    "no:cacheprovider",
    "--html=pytest_report/index.html",
    "--durations=10",
    "/home/runner/work/functionapp/functionapp",
]

print(f"Running: {' '.join(cmd)}")  # noqa
run(cmd, check=True, cwd=root)
#run(["coverage", "erase", "{root}"], check=True, cwd=root, shell=True)