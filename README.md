# pytest-battle 🐍⚔️

A **Rustlings-inspired** Python learning environment where you learn by fixing broken code and making tests pass.

## Overview

pytest-battle is designed to help you learn Python through hands-on practice. Each exercise contains:

- **Broken code** with `TODO` markers showing what needs to be fixed
- **Tests** that verify your solution is correct
- **Hints** to help when you're stuck

Your goal: **Make all the tests pass!**

## Difficulty Levels

| Level | Focus Areas | Prerequisites |
|-------|------------|---------------|
| **Junior** | Variables, strings, lists, loops, basic functions | None |
| **Mid** | OOP, decorators, generators, comprehensions, error handling | Junior level |
| **Senior** | Concurrency, design patterns, algorithms, metaclasses | Mid level |

## Quick Start

### 1. Install dependencies

```bash
# Using uv (recommended)
uv sync --extra dev

# Or using pip
pip install -e ".[dev]"
```

### 2. List all exercises

```bash
# Using the CLI
uv run battle list

# Or directly with Python
python -m pytest_battle.cli list
```

### 3. Run exercises

```bash
# Run ALL exercises
uv run battle run

# Run a specific level
uv run battle run --level junior

# Run a specific exercise
uv run battle run --exercise ex01_variables
```

### 4. Check your progress

```bash
uv run battle verify
```

### 5. Get hints

```bash
uv run battle hint ex01_variables
```

### 6. Launch the Steampunk TUI

```bash
uv run battle-tui
```

This launches an interactive terminal interface with:
- **Steam-powered aesthetics** - Brass, copper, and industrial elegance
- **Exercise browser** - Navigate all levels and exercises
- **Live test running** - See results in real-time
- **Progress gauges** - Track your advancement
- **Hint viewer** - Get help when stuck

**TUI Controls:**
| Key | Action |
|-----|--------|
| `R` | Run tests for selected exercise |
| `H` | Show hint |
| `F` | Refresh progress |
| `Q` | Quit |

## How to Solve Exercises

1. **Navigate** to an exercise folder (e.g., `exercises/01_junior/ex01_variables/`)
2. **Read** the `README.md` for the exercise description
3. **Open** `exercise.py` and look for `TODO` comments
4. **Fix** the code to make the tests pass
5. **Run** `uv run pytest exercises/01_junior/ex01_variables/` to check your solution
6. **Repeat** until all tests are green!

## Project Structure

```
pytest-battle/
├── exercises/
│   ├── 01_junior/           # Beginner exercises
│   │   ├── README.md
│   │   ├── ex01_variables/
│   │   │   ├── README.md
│   │   │   ├── exercise.py  # Fix this file!
│   │   │   ├── test_exercise.py
│   │   │   └── HINT.md
│   │   └── ...
│   ├── 02_mid/              # Intermediate exercises
│   │   └── ...
│   └── 03_senior/           # Advanced exercises
│       └── ...
├── src/pytest_battle/       # CLI tool
├── pyproject.toml
└── README.md
```

## Running Tests Directly

You can also use pytest directly:

```bash
# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v

# Run with coverage
uv run pytest --cov=exercises --cov-report=term-missing

# Run specific level
uv run pytest exercises/01_junior/

# Run specific exercise
uv run pytest exercises/01_junior/ex01_variables/
```

## Progress Tracking

Your progress is measured by the number of passing tests:

```bash
# Quick progress check
uv run battle verify

# Detailed coverage report
uv run battle coverage
```

## Success Criteria

| Level | To Complete |
|-------|-------------|
| **Junior** | All Junior tests passing (100%) |
| **Mid** | All Junior + Mid tests passing (100%) |
| **Senior** | All tests passing (100%) |

## Tips for Success

1. **Read the test file** - It shows exactly what's expected
2. **Start with Junior** - Build fundamentals before advancing
3. **Use hints sparingly** - Try first, then ask for help
4. **Run tests often** - Small iterations are better
5. **Read error messages** - pytest tells you what went wrong

## Contributing

Want to add exercises? Great! Each exercise needs:

1. `README.md` - Description and learning objectives
2. `exercise.py` - Code with `TODO` markers
3. `test_exercise.py` - Tests that verify the solution
4. `HINT.md` - Helpful hints (without giving away the answer)

## License

MIT License - See [LICENSE](LICENSE) for details.

---

**Happy coding! May your tests be green! 🟢**
