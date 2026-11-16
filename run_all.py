"""Run all nine report-based calculation examples with one command."""

from pathlib import Path
import subprocess
import sys


def main():
    directory = Path(__file__).resolve().parent
    scripts = sorted(directory.glob("[0-9][0-9]_*.py"))
    if len(scripts) != 9:
        raise SystemExit("Expected nine numbered calculation files alongside run_all.py.")
    for script in scripts:
        print(f"\n--- {script.name} ---", flush=True)
        subprocess.run([sys.executable, str(script)], check=True)


if __name__ == "__main__":
    main()
