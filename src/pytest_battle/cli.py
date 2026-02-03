#!/usr/bin/env python3
"""CLI for pytest-battle - run and track your Python learning progress."""

import argparse
import subprocess
import sys
from pathlib import Path


EXERCISES_DIR = Path(__file__).parent.parent.parent / "exercises"

LEVELS = {
    "junior": "01_junior",
    "mid": "02_mid",
    "senior": "03_senior",
}

LEVEL_DESCRIPTIONS = {
    "junior": "Python fundamentals: variables, strings, lists, functions",
    "mid": "Intermediate: OOP, decorators, generators, comprehensions",
    "senior": "Advanced: concurrency, patterns, algorithms, metaclasses",
}


def get_exercise_dirs(level: str | None = None) -> list[Path]:
    """Get all exercise directories, optionally filtered by level."""
    if level:
        level_dir = EXERCISES_DIR / LEVELS.get(level, level)
        if not level_dir.exists():
            return []
        return sorted([d for d in level_dir.iterdir() if d.is_dir() and d.name.startswith("ex")])

    all_exercises = []
    for level_name in LEVELS.values():
        level_dir = EXERCISES_DIR / level_name
        if level_dir.exists():
            all_exercises.extend(sorted([d for d in level_dir.iterdir() if d.is_dir() and d.name.startswith("ex")]))
    return all_exercises


def run_tests(path: Path | None = None, verbose: bool = True, coverage: bool = False) -> int:
    """Run pytest on the specified path."""
    cmd = ["python", "-m", "pytest"]

    if verbose:
        cmd.append("-v")

    if coverage:
        cmd.extend(["--cov=exercises", "--cov-report=term-missing"])

    if path:
        cmd.append(str(path))
    else:
        cmd.append(str(EXERCISES_DIR))

    result = subprocess.run(cmd, cwd=EXERCISES_DIR.parent)
    return result.returncode


def cmd_list(args: argparse.Namespace) -> int:
    """List all available exercises."""
    print("\n" + "=" * 60)
    print("  PYTEST-BATTLE EXERCISES")
    print("=" * 60 + "\n")

    for level, level_dir in LEVELS.items():
        print(f"\n{'─' * 40}")
        print(f"  {level.upper()} LEVEL")
        print(f"  {LEVEL_DESCRIPTIONS[level]}")
        print(f"{'─' * 40}")

        exercises = get_exercise_dirs(level)
        if not exercises:
            print("  (no exercises yet)")
            continue

        for ex in exercises:
            # Check if tests pass
            result = subprocess.run(
                ["python", "-m", "pytest", str(ex), "-q", "--tb=no"],
                capture_output=True,
                cwd=EXERCISES_DIR.parent
            )
            status = "✓" if result.returncode == 0 else "○"
            print(f"  {status} {ex.name}")

    print("\n" + "=" * 60)
    print("  Legend: ✓ = completed, ○ = pending")
    print("=" * 60 + "\n")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    """Run exercises."""
    level = args.level
    exercise = args.exercise

    if exercise:
        # Find the specific exercise
        for lvl in LEVELS.values():
            ex_path = EXERCISES_DIR / lvl / exercise
            if ex_path.exists():
                print(f"\n Running exercise: {exercise}\n")
                return run_tests(ex_path, verbose=True)

        print(f"Exercise '{exercise}' not found.")
        return 1

    if level:
        level_path = EXERCISES_DIR / LEVELS.get(level, level)
        if not level_path.exists():
            print(f"Level '{level}' not found.")
            return 1
        print(f"\n Running all {level.upper()} exercises\n")
        return run_tests(level_path, verbose=True)

    print("\n Running ALL exercises\n")
    return run_tests(verbose=True)


def cmd_verify(args: argparse.Namespace) -> int:
    """Verify all exercises and show progress."""
    print("\n" + "=" * 60)
    print("  VERIFICATION & PROGRESS REPORT")
    print("=" * 60 + "\n")

    total = 0
    passed = 0

    for level, level_dir in LEVELS.items():
        exercises = get_exercise_dirs(level)
        level_passed = 0
        level_total = len(exercises)
        total += level_total

        print(f"\n{level.upper()} LEVEL:")

        for ex in exercises:
            result = subprocess.run(
                ["python", "-m", "pytest", str(ex), "-q", "--tb=no"],
                capture_output=True,
                cwd=EXERCISES_DIR.parent
            )
            if result.returncode == 0:
                level_passed += 1
                passed += 1
                print(f"  ✓ {ex.name}")
            else:
                print(f"  ✗ {ex.name}")

        if level_total > 0:
            pct = (level_passed / level_total) * 100
            print(f"  Progress: {level_passed}/{level_total} ({pct:.0f}%)")

    print("\n" + "=" * 60)
    if total > 0:
        overall_pct = (passed / total) * 100
        print(f"  OVERALL PROGRESS: {passed}/{total} exercises ({overall_pct:.0f}%)")

        # Progress bar
        bar_len = 40
        filled = int(bar_len * passed / total)
        bar = "█" * filled + "░" * (bar_len - filled)
        print(f"  [{bar}]")
    else:
        print("  No exercises found.")
    print("=" * 60 + "\n")

    return 0 if passed == total else 1


def cmd_hint(args: argparse.Namespace) -> int:
    """Show hint for an exercise."""
    exercise = args.exercise

    for lvl in LEVELS.values():
        hint_path = EXERCISES_DIR / lvl / exercise / "HINT.md"
        if hint_path.exists():
            print(f"\n{'─' * 40}")
            print(f"  HINT for {exercise}")
            print(f"{'─' * 40}\n")
            print(hint_path.read_text())
            return 0

    print(f"No hint found for exercise '{exercise}'.")
    return 1


def cmd_coverage(args: argparse.Namespace) -> int:
    """Run tests with coverage report."""
    print("\n Running tests with coverage...\n")
    return run_tests(coverage=True)


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        prog="battle",
        description="pytest-battle: A Rustlings-inspired Python learning environment",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # list command
    list_parser = subparsers.add_parser("list", help="List all exercises")
    list_parser.set_defaults(func=cmd_list)

    # run command
    run_parser = subparsers.add_parser("run", help="Run exercises")
    run_parser.add_argument("-l", "--level", choices=["junior", "mid", "senior"],
                           help="Run only exercises from this level")
    run_parser.add_argument("-e", "--exercise", help="Run a specific exercise")
    run_parser.set_defaults(func=cmd_run)

    # verify command
    verify_parser = subparsers.add_parser("verify", help="Verify progress")
    verify_parser.set_defaults(func=cmd_verify)

    # hint command
    hint_parser = subparsers.add_parser("hint", help="Show hint for an exercise")
    hint_parser.add_argument("exercise", help="Exercise name (e.g., ex01_variables)")
    hint_parser.set_defaults(func=cmd_hint)

    # coverage command
    cov_parser = subparsers.add_parser("coverage", help="Run with coverage report")
    cov_parser.set_defaults(func=cmd_coverage)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
