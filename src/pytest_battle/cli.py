#!/usr/bin/env python3
"""CLI for pytest-battle - run and track your Python learning progress."""

import argparse
import re
import subprocess
import sys
from pathlib import Path


_ANSI_RE = re.compile(r"\033\[[0-9;]*m")


def visual_len(s: str) -> int:
    """Return the printable length of s, ignoring ANSI escape codes."""
    return len(_ANSI_RE.sub("", s))


# ── ANSI color helpers ────────────────────────────────────────────────────────

def _supports_color() -> bool:
    return hasattr(sys.stdout, "isatty") and sys.stdout.isatty()


class C:
    """ANSI escape codes — silently disabled when stdout is not a TTY."""
    _on = _supports_color()

    RESET   = "\033[0m"  if _on else ""
    BOLD    = "\033[1m"  if _on else ""
    DIM     = "\033[2m"  if _on else ""
    RED     = "\033[91m" if _on else ""
    GREEN   = "\033[92m" if _on else ""
    YELLOW  = "\033[93m" if _on else ""
    BLUE    = "\033[94m" if _on else ""
    MAGENTA = "\033[95m" if _on else ""
    CYAN    = "\033[96m" if _on else ""
    WHITE   = "\033[97m" if _on else ""


def col(text: str, *codes: str) -> str:
    """Wrap *text* with ANSI *codes* and append a reset."""
    if not codes:
        return text
    return "".join(codes) + text + C.RESET


# ── Constants ─────────────────────────────────────────────────────────────────

EXERCISES_DIR = Path(__file__).parent.parent.parent / "exercises"

LEVELS = {
    "junior": "01_junior",
    "mid":    "02_mid",
    "senior": "03_senior",
}

LEVEL_DESCRIPTIONS = {
    "junior": "Python fundamentals: variables, strings, lists, functions",
    "mid":    "Intermediate: OOP, decorators, generators, comprehensions",
    "senior": "Advanced: concurrency, patterns, algorithms, metaclasses",
}

LEVEL_COLORS = {
    "junior": C.CYAN,
    "mid":    C.YELLOW,
    "senior": C.MAGENTA,
}


# ── Helpers ───────────────────────────────────────────────────────────────────

def get_exercise_dirs(level: str | None = None) -> list[Path]:
    """Return exercise directories, optionally filtered by level."""
    if level:
        level_dir = EXERCISES_DIR / LEVELS.get(level, level)
        if not level_dir.exists():
            return []
        return sorted([d for d in level_dir.iterdir() if d.is_dir() and d.name.startswith("ex")])

    all_exercises = []
    for level_name in LEVELS.values():
        level_dir = EXERCISES_DIR / level_name
        if level_dir.exists():
            all_exercises.extend(
                sorted([d for d in level_dir.iterdir() if d.is_dir() and d.name.startswith("ex")])
            )
    return all_exercises


def run_tests(path: Path | None = None, verbose: bool = True, coverage: bool = False) -> int:
    """Run pytest on the given path and return the exit code."""
    cmd = [sys.executable, "-m", "pytest"]
    if verbose:
        cmd.append("-v")
    if coverage:
        cmd.extend(["--cov=exercises", "--cov-report=term-missing"])
    cmd.append(str(path) if path else str(EXERCISES_DIR))
    return subprocess.run(cmd, cwd=EXERCISES_DIR.parent).returncode


def exercise_passed(ex_path: Path) -> bool:
    """Return True if all tests in ex_path pass (silent)."""
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(ex_path), "-q", "--tb=no"],
        capture_output=True,
        cwd=EXERCISES_DIR.parent,
    )
    return result.returncode == 0


def print_banner() -> None:
    """Print the main pytest-battle banner."""
    w = 62  # inner content width (between the two ║ chars)
    bc = C.CYAN

    border  = col("╔" + "═" * w + "╗", bc, C.BOLD)
    mid_sep = col("╠" + "═" * w + "╣", bc, C.BOLD)
    bottom  = col("╚" + "═" * w + "╝", bc, C.BOLD)
    pipe    = col("║", bc, C.BOLD)

    def row(content: str = "") -> str:
        """Build a padded box row from (possibly coloured) content."""
        pad = max(0, w - visual_len(content) - 2)  # -2 for the leading "  "
        return f"{pipe}  {content}{' ' * pad}{pipe}"

    commands = [
        ("battle list",                  "List all exercises with status"),
        ("battle run",                   "Run all exercises"),
        ("battle run -l mid",            "Run a level  (junior / mid / senior)"),
        ("battle run -e ex01_variables", "Run one exercise by name"),
        ("battle verify",                "Full progress report"),
        ("battle hint <name>",           "Show hints for an exercise"),
        ("battle coverage",              "Run tests with coverage"),
    ]

    print()
    print(border)
    print(row())
    print(row(col("⚡  pytest-battle", C.WHITE, C.BOLD)))
    print(row(col("Python learning through test-driven exercises", C.DIM)))
    print(row())
    print(mid_sep)
    print(row())

    for cmd_text, desc in commands:
        content = col(cmd_text, C.GREEN, C.BOLD) + col("  " + desc, C.DIM)
        print(row(content))

    print(row())
    print(bottom)
    print()


def print_section_header(title: str, color: str = C.BLUE) -> None:
    line = col("─" * 56, color)
    print(f"\n  {line}")
    print(f"  {col('  ' + title, color, C.BOLD)}")
    print(f"  {line}")


# ── Commands ──────────────────────────────────────────────────────────────────

def cmd_list(args: argparse.Namespace) -> int:
    """List all available exercises."""
    print()
    title_bar = col("  PYTEST-BATTLE EXERCISES  ", C.BLUE, C.BOLD)
    border    = col("═" * 56, C.BLUE)
    print(f"  {border}")
    print(f"  {title_bar}")
    print(f"  {border}")

    for level, _level_dir in LEVELS.items():
        lc = LEVEL_COLORS[level]
        print()
        print(f"  {col('─' * 50, lc)}")
        print(f"  {col(level.upper() + ' LEVEL', lc, C.BOLD)}  "
              f"{col(LEVEL_DESCRIPTIONS[level], C.DIM)}")
        print(f"  {col('─' * 50, lc)}")

        exercises = get_exercise_dirs(level)
        if not exercises:
            print(f"    {col('(no exercises yet)', C.DIM)}")
            continue

        for ex in exercises:
            passed = exercise_passed(ex)
            if passed:
                symbol = col("✓", C.GREEN, C.BOLD)
                name   = col(ex.name, C.GREEN)
                badge  = col(" done", C.GREEN, C.DIM)
            else:
                symbol = col("○", C.DIM)
                name   = ex.name
                badge  = col(" pending", C.DIM)
            print(f"    {symbol}  {name}{badge}")

    print()
    print(f"  {col('─' * 50, C.BLUE)}")
    print(f"  {col('✓', C.GREEN, C.BOLD)} completed   "
          f"{col('○', C.DIM)} pending")
    print(f"  {col('─' * 50, C.BLUE)}")
    print()
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Run exercises."""
    level    = args.level
    exercise = args.exercise

    if exercise:
        for lvl in LEVELS.values():
            ex_path = EXERCISES_DIR / lvl / exercise
            if ex_path.exists():
                print()
                print(f"  {col('▶  Running exercise:', C.CYAN, C.BOLD)}  "
                      f"{col(exercise, C.WHITE, C.BOLD)}")
                print()
                return run_tests(ex_path, verbose=True)
        print(f"\n  {col('✗  Exercise not found:', C.RED, C.BOLD)} {exercise}\n")
        return 1

    if level:
        level_path = EXERCISES_DIR / LEVELS.get(level, level)
        if not level_path.exists():
            print(f"\n  {col('✗  Level not found:', C.RED, C.BOLD)} {level}\n")
            return 1
        lc = LEVEL_COLORS[level]
        print()
        print(f"  {col('▶  Running all', C.CYAN, C.BOLD)}  "
              f"{col(level.upper() + ' LEVEL', lc, C.BOLD)}  "
              f"{col('exercises', C.CYAN, C.BOLD)}")
        print()
        return run_tests(level_path, verbose=True)

    print()
    print(f"  {col('▶  Running', C.CYAN, C.BOLD)}  "
          f"{col('ALL', C.WHITE, C.BOLD)}  {col('exercises', C.CYAN, C.BOLD)}")
    print()
    return run_tests(verbose=True)


def cmd_verify(args: argparse.Namespace) -> int:
    """Verify all exercises and show a colour-coded progress report."""
    print()
    border = col("═" * 56, C.BLUE)
    print(f"  {border}")
    print(f"  {col('  VERIFICATION & PROGRESS REPORT  ', C.BLUE, C.BOLD)}")
    print(f"  {border}")

    total  = 0
    passed = 0

    for level, _level_dir in LEVELS.items():
        exercises    = get_exercise_dirs(level)
        level_passed = 0
        level_total  = len(exercises)
        total       += level_total
        lc           = LEVEL_COLORS[level]

        print()
        print(f"  {col(level.upper() + ' LEVEL', lc, C.BOLD)}")

        for ex in exercises:
            if exercise_passed(ex):
                level_passed += 1
                passed       += 1
                mark = col("  ✓", C.GREEN, C.BOLD)
                name = col(ex.name, C.GREEN)
            else:
                mark = col("  ✗", C.RED, C.BOLD)
                name = col(ex.name, C.DIM)
            print(f"    {mark}  {name}")

        if level_total > 0:
            pct = level_passed / level_total * 100
            bar_len  = 20
            filled   = int(bar_len * level_passed / level_total)
            bar      = col("█" * filled, lc, C.BOLD) + col("░" * (bar_len - filled), C.DIM)
            pct_text = col(f"{pct:.0f}%", lc, C.BOLD)
            print(f"    {col('[', C.DIM)}{bar}{col(']', C.DIM)}"
                  f"  {col(str(level_passed), lc, C.BOLD)}{col('/' + str(level_total), C.DIM)}"
                  f"  {pct_text}")

    print()
    print(f"  {border}")
    if total > 0:
        overall_pct = passed / total * 100
        bar_len  = 40
        filled   = int(bar_len * passed / total)

        if overall_pct == 100:
            bar_color = C.GREEN
        elif overall_pct >= 50:
            bar_color = C.YELLOW
        else:
            bar_color = C.RED

        bar      = col("█" * filled, bar_color, C.BOLD) + col("░" * (bar_len - filled), C.DIM)
        pct_text = col(f"{overall_pct:.0f}%", bar_color, C.BOLD)
        print()
        print(f"  {col('OVERALL PROGRESS', C.WHITE, C.BOLD)}")
        print(f"  {col('[', C.DIM)}{bar}{col(']', C.DIM)}  "
              f"{col(str(passed), bar_color, C.BOLD)}{col('/' + str(total), C.DIM)}"
              f"  {pct_text}")
        print()

        if overall_pct == 100:
            print(f"  {col('🎉  All exercises complete!  Great work!', C.GREEN, C.BOLD)}")
        else:
            remaining = total - passed
            print(f"  {col(str(remaining) + ' exercise(s) remaining.', C.DIM)}"
                  f"  {col('Keep going!', C.YELLOW)}")
    else:
        print(f"  {col('No exercises found.', C.DIM)}")

    print()
    print(f"  {border}")
    print()
    return 0 if passed == total else 1


def cmd_hint(args: argparse.Namespace) -> int:
    """Show hint for an exercise."""
    exercise = args.exercise

    for lvl in LEVELS.values():
        hint_path = EXERCISES_DIR / lvl / exercise / "HINT.md"
        if hint_path.exists():
            print()
            print(f"  {col('─' * 50, C.YELLOW)}")
            print(f"  {col('💡  HINT for ' + exercise, C.YELLOW, C.BOLD)}")
            print(f"  {col('─' * 50, C.YELLOW)}")
            print()
            for line in hint_path.read_text().splitlines():
                if line.startswith("## "):
                    print(col("  " + line, C.CYAN, C.BOLD))
                elif line.startswith("# "):
                    print(col("  " + line, C.WHITE, C.BOLD))
                elif line.startswith("```"):
                    print(col("  " + line, C.DIM))
                else:
                    print("  " + line)
            print()
            return 0

    print(f"\n  {col('✗  No hint found for:', C.RED, C.BOLD)} {exercise}\n")
    return 1


def cmd_coverage(args: argparse.Namespace) -> int:
    """Run tests with coverage report."""
    print()
    print(f"  {col('📊  Running tests with coverage...', C.CYAN, C.BOLD)}")
    print()
    return run_tests(coverage=True)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="battle",
        description="pytest-battle: A Rustlings-inspired Python learning environment",
        add_help=True,
    )
    subparsers = parser.add_subparsers(dest="command")

    list_parser = subparsers.add_parser("list", help="List all exercises with status")
    list_parser.set_defaults(func=cmd_list)

    run_parser = subparsers.add_parser("run", help="Run exercises")
    run_parser.add_argument("-l", "--level", choices=["junior", "mid", "senior"],
                            help="Run only this level")
    run_parser.add_argument("-e", "--exercise", help="Run a single exercise by name")
    run_parser.set_defaults(func=cmd_run)

    verify_parser = subparsers.add_parser("verify", help="Show progress report")
    verify_parser.set_defaults(func=cmd_verify)

    hint_parser = subparsers.add_parser("hint", help="Show hint for an exercise")
    hint_parser.add_argument("exercise", help="Exercise name (e.g., ex01_variables)")
    hint_parser.set_defaults(func=cmd_hint)

    cov_parser = subparsers.add_parser("coverage", help="Run with coverage report")
    cov_parser.set_defaults(func=cmd_coverage)

    args = parser.parse_args()

    if not args.command:
        print_banner()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
