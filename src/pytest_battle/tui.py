#!/usr/bin/env python3
"""
Simple TUI for pytest-battle - an interactive terminal interface
for learning Python through exercises.
"""

import subprocess
import sys
from pathlib import Path
from typing import ClassVar

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import (
    Button,
    Footer,
    Header,
    Label,
    ProgressBar,
    RichLog,
    Static,
    Tree,
)
from textual.widgets.tree import TreeNode


# Simple CSS theme using Textual defaults
SIMPLE_CSS = """
Screen {
    background: $surface;
}

#main-container {
    layout: horizontal;
    height: 100%;
}

#sidebar {
    width: 40;
    border-right: solid $primary;
}

#content {
    width: 1fr;
}

#exercise-tree {
    height: 1fr;
    padding: 1;
}

#progress-section {
    height: auto;
    border: solid $primary;
    margin: 1;
    padding: 1;
}

#progress-title {
    text-align: center;
    text-style: bold;
    margin-bottom: 1;
}

.progress-row {
    height: 3;
    margin-bottom: 1;
}

.progress-label {
    width: 15;
}

ProgressBar {
    width: 1fr;
}

#progress-text {
    text-align: center;
    margin-top: 1;
}

#button-bar {
    height: auto;
    align: center middle;
    margin: 1;
}

Button {
    margin: 0 1;
}

#info-section {
    height: auto;
    max-height: 15;
    border: solid $primary;
    margin: 1;
    padding: 1;
}

#info-title {
    text-align: center;
    text-style: bold;
    margin-bottom: 1;
}

#info-content {
    padding: 1;
}

#output-section {
    height: 1fr;
    border: solid $primary;
    margin: 1;
}

#output-title {
    text-align: center;
    text-style: bold;
    padding: 1;
    border-bottom: solid $primary;
}

#test-output {
    padding: 1;
}
"""


# Helper functions
def get_exercises_dir() -> Path:
    """Get the exercises directory."""
    return Path(__file__).parent.parent.parent / "exercises"


def get_exercise_status(exercise_path: Path) -> str:
    """Run tests for an exercise and return status."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(exercise_path), "-q", "--tb=no"],
            capture_output=True,
            timeout=30,
            cwd=exercise_path.parent.parent.parent,
        )
        return "passed" if result.returncode == 0 else "failed"
    except Exception:
        return "failed"


def run_exercise_tests(exercise_path: Path) -> tuple[str, str, int]:
    """Run tests for an exercise and return (stdout, stderr, returncode)."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(exercise_path), "-v", "--tb=short"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=exercise_path.parent.parent.parent,
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Test execution timed out!", 1
    except Exception as e:
        return "", f"Error running tests: {e}", 1


def count_exercises() -> dict[str, tuple[int, int]]:
    """Count passed/total exercises per level."""
    exercises_dir = get_exercises_dir()
    counts = {}

    for level_dir in sorted(exercises_dir.iterdir()):
        if not level_dir.is_dir():
            continue

        level_name = level_dir.name.split("_", 1)[-1] if "_" in level_dir.name else level_dir.name
        passed = 0
        total = 0

        for ex_dir in sorted(level_dir.iterdir()):
            if ex_dir.is_dir() and ex_dir.name.startswith("ex"):
                total += 1
                if get_exercise_status(ex_dir) == "passed":
                    passed += 1

        counts[level_name] = (passed, total)

    return counts


# Custom widgets
class ExerciseInfo(Static):
    """Display information about selected exercise."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exercise_name = ""
        self.exercise_level = ""
        self.exercise_status = "pending"

    def compose(self) -> ComposeResult:
        yield Static("Exercise Info", id="info-title")
        yield Static("Select an exercise to view details", id="info-content")

    def update_info(self, name: str, level: str, status: str, description: str = ""):
        """Update the exercise information display."""
        self.exercise_name = name
        self.exercise_level = level
        self.exercise_status = status

        status_symbol = "✓" if status == "passed" else "○"

        content = f"""[bold]{name}[/bold]

Level: {level.upper()}
Status: {status_symbol} {status.upper()}

{description}
        """.strip()

        self.query_one("#info-content", Static).update(content)


# Main TUI Application
class PytestBattleTUI(App):
    """The main Pytest Battle TUI application."""

    TITLE = "Pytest Battle"
    CSS = SIMPLE_CSS

    BINDINGS: ClassVar[list[Binding]] = [
        Binding("q", "quit", "Quit", show=True),
        Binding("r", "run_tests", "Run Tests", show=True),
        Binding("h", "show_hint", "Show Hint", show=True),
        Binding("f", "refresh", "Refresh", show=True),
    ]

    selected_exercise: reactive[Path | None] = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main-container"):
            # Left sidebar with exercise tree
            with Vertical(id="sidebar"):
                yield Tree("Exercises", id="exercise-tree")

            # Right content area
            with Vertical(id="content"):
                # Progress section
                with Vertical(id="progress-section"):
                    yield Static("Progress", id="progress-title")

                    with Horizontal(classes="progress-row"):
                        yield Label("Junior:", classes="progress-label")
                        yield ProgressBar(total=100, show_eta=False, id="junior-progress")

                    with Horizontal(classes="progress-row"):
                        yield Label("Mid:", classes="progress-label")
                        yield ProgressBar(total=100, show_eta=False, id="mid-progress")

                    with Horizontal(classes="progress-row"):
                        yield Label("Senior:", classes="progress-label")
                        yield ProgressBar(total=100, show_eta=False, id="senior-progress")

                    yield Static("", id="progress-text")

                # Button bar
                with Horizontal(id="button-bar"):
                    yield Button("Run Tests", id="run-btn", variant="primary")
                    yield Button("Hint", id="hint-btn")
                    yield Button("Refresh", id="refresh-btn")

                # Exercise info
                with Vertical(id="info-section"):
                    yield ExerciseInfo(id="exercise-info")

                # Test output
                with Vertical(id="output-section"):
                    yield Static("Test Output", id="output-title")
                    yield RichLog(id="test-output", highlight=True, markup=True)

        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app when mounted."""
        self.populate_tree()
        self.update_progress()
        self.write_welcome_message()

    def write_welcome_message(self) -> None:
        """Write welcome message to output."""
        output = self.query_one("#test-output", RichLog)
        output.write("=" * 60)
        output.write("Welcome to Pytest Battle!")
        output.write("=" * 60)
        output.write("")
        output.write("Select an exercise from the tree on the left,")
        output.write("then press R or click Run Tests to test your solution.")
        output.write("")
        output.write("Press H for hints when you're stuck.")
        output.write("Press Q to quit.")
        output.write("")

    def populate_tree(self) -> None:
        """Populate the exercise tree."""
        tree = self.query_one("#exercise-tree", Tree)
        tree.clear()
        tree.root.expand()

        exercises_dir = get_exercises_dir()

        level_names = {
            "01_junior": ("Junior", "junior"),
            "02_mid": ("Mid", "mid"),
            "03_senior": ("Senior", "senior"),
        }

        for level_dir in sorted(exercises_dir.iterdir()):
            if not level_dir.is_dir():
                continue

            display_name, level_key = level_names.get(
                level_dir.name,
                (level_dir.name, "unknown")
            )
            level_node = tree.root.add(f"[bold]{display_name}[/]", expand=True)
            level_node.data = {"type": "level", "path": level_dir}

            for ex_dir in sorted(level_dir.iterdir()):
                if not ex_dir.is_dir() or not ex_dir.name.startswith("ex"):
                    continue

                # Get status
                status = get_exercise_status(ex_dir)
                status_symbol = "✓" if status == "passed" else "○"

                # Format exercise name
                ex_name = ex_dir.name.replace("_", " ").title()

                if status == "passed":
                    label = f"[green]{status_symbol} {ex_name}[/]"
                else:
                    label = f"{status_symbol} {ex_name}"

                ex_node = level_node.add_leaf(label)
                ex_node.data = {
                    "type": "exercise",
                    "path": ex_dir,
                    "level": level_key,
                    "status": status,
                }

    def update_progress(self) -> None:
        """Update progress bars."""
        counts = count_exercises()

        total_passed = 0
        total_exercises = 0

        for level, (passed, total) in counts.items():
            total_passed += passed
            total_exercises += total

            progress_pct = (passed / total * 100) if total > 0 else 0

            try:
                widget_id = f"{level}-progress"
                progress_widget = self.query_one(f"#{widget_id}", ProgressBar)
                progress_widget.update(progress=progress_pct)
            except Exception:
                pass

        # Update overall progress text
        overall_pct = (total_passed / total_exercises * 100) if total_exercises > 0 else 0
        progress_text = self.query_one("#progress-text", Static)
        progress_text.update(
            f"Overall: {total_passed}/{total_exercises} ({overall_pct:.0f}%)"
        )

    @on(Tree.NodeSelected)
    def on_tree_select(self, event: Tree.NodeSelected) -> None:
        """Handle tree node selection."""
        node = event.node
        if node.data and node.data.get("type") == "exercise":
            self.selected_exercise = node.data["path"]

            # Update info panel
            info = self.query_one("#exercise-info", ExerciseInfo)
            info.update_info(
                name=node.data["path"].name,
                level=node.data["level"],
                status=node.data["status"],
                description="Press R to run tests for this exercise.",
            )

    @on(Button.Pressed, "#run-btn")
    def on_run_button(self) -> None:
        """Handle run button press."""
        self.action_run_tests()

    @on(Button.Pressed, "#hint-btn")
    def on_hint_button(self) -> None:
        """Handle hint button press."""
        self.action_show_hint()

    @on(Button.Pressed, "#refresh-btn")
    def on_refresh_button(self) -> None:
        """Handle refresh button press."""
        self.action_refresh()

    def action_run_tests(self) -> None:
        """Run tests for selected exercise."""
        if not self.selected_exercise:
            output = self.query_one("#test-output", RichLog)
            output.write("[bold red]No exercise selected![/]")
            output.write("Select an exercise from the tree first.")
            return

        self.run_tests_worker()

    @work(exclusive=True, thread=True)
    def run_tests_worker(self) -> None:
        """Run tests in a worker thread."""
        if not self.selected_exercise:
            return

        exercise_path = self.selected_exercise

        # Update UI to show running
        self.call_from_thread(self._show_running, exercise_path.name)

        # Run tests
        stdout, stderr, returncode = run_exercise_tests(exercise_path)

        # Update UI with results
        self.call_from_thread(self._show_results, stdout, stderr, returncode)

        # Refresh progress
        self.call_from_thread(self.update_progress)
        self.call_from_thread(self.populate_tree)

    def _show_running(self, name: str) -> None:
        """Show running status in output."""
        output = self.query_one("#test-output", RichLog)
        output.clear()
        output.write(f"[bold]Running tests for {name}[/]")
        output.write("")
        output.write("Running...")
        output.write("")

    def _show_results(self, stdout: str, stderr: str, returncode: int) -> None:
        """Show test results in output."""
        output = self.query_one("#test-output", RichLog)
        output.clear()

        if returncode == 0:
            output.write("[bold green]" + "=" * 50 + "[/]")
            output.write("[bold green]ALL TESTS PASSED![/]")
            output.write("[bold green]" + "=" * 50 + "[/]")
        else:
            output.write("[bold red]" + "=" * 50 + "[/]")
            output.write("[bold red]SOME TESTS FAILED[/]")
            output.write("[bold red]" + "=" * 50 + "[/]")

        output.write("")

        if stdout:
            for line in stdout.split("\n"):
                # Color code the output
                if "PASSED" in line:
                    output.write(f"[green]{line}[/]")
                elif "FAILED" in line:
                    output.write(f"[red]{line}[/]")
                elif "ERROR" in line:
                    output.write(f"[yellow]{line}[/]")
                else:
                    output.write(line)

        if stderr:
            output.write("")
            output.write("[bold yellow]Errors:[/]")
            output.write(f"[yellow]{stderr}[/]")

    def action_show_hint(self) -> None:
        """Show hint for selected exercise."""
        if not self.selected_exercise:
            output = self.query_one("#test-output", RichLog)
            output.write("[bold red]No exercise selected![/]")
            return

        hint_path = self.selected_exercise / "HINT.md"
        output = self.query_one("#test-output", RichLog)
        output.clear()

        if hint_path.exists():
            output.write("=" * 50)
            output.write(f"[bold]HINT for {self.selected_exercise.name}[/]")
            output.write("=" * 50)
            output.write("")

            content = hint_path.read_text()
            for line in content.split("\n"):
                if line.startswith("#"):
                    output.write(f"[bold]{line}[/]")
                else:
                    output.write(line)
        else:
            output.write("[red]No hint available for this exercise.[/]")

    def action_refresh(self) -> None:
        """Refresh the exercise tree and progress."""
        output = self.query_one("#test-output", RichLog)
        output.clear()
        output.write("Refreshing...")

        self.populate_tree()
        self.update_progress()

        output.write("[green]Refreshed![/]")


# Entry point
def main() -> None:
    """Run the Pytest Battle TUI."""
    app = PytestBattleTUI()
    app.run()


if __name__ == "__main__":
    main()
