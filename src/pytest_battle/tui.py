#!/usr/bin/env python3
"""
Pytest Battle TUI - A fast, simple terminal interface for Python exercises.
"""

import subprocess
import sys
from pathlib import Path
from typing import ClassVar

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.widgets import (
    Button,
    Footer,
    Header,
    Label,
    RichLog,
    Static,
    Tree,
)


# ═══════════════════════════════════════════════════════════════════════════════
# SIMPLE CSS - Fast to render
# ═══════════════════════════════════════════════════════════════════════════════

SIMPLE_CSS = """
Screen {
    background: #1a1a2e;
}

Header {
    background: #16213e;
    color: #e94560;
}

Footer {
    background: #16213e;
    color: #0f3460;
}

#main-container {
    layout: horizontal;
}

#sidebar {
    width: 35;
    background: #16213e;
    border-right: solid #0f3460;
    padding: 1;
}

#sidebar-title {
    text-align: center;
    text-style: bold;
    color: #e94560;
    padding: 1;
}

#exercise-tree {
    background: transparent;
}

Tree {
    background: transparent;
}

Tree > .tree--cursor {
    background: #0f3460;
    color: #eee;
}

#content {
    width: 1fr;
    padding: 1;
}

#info-panel {
    height: 6;
    background: #16213e;
    border: solid #0f3460;
    padding: 1;
    margin-bottom: 1;
}

#info-title {
    color: #e94560;
    text-style: bold;
}

#info-text {
    color: #eee;
}

#button-bar {
    height: 3;
    margin-bottom: 1;
}

Button {
    margin-right: 1;
}

#output-panel {
    height: 1fr;
    background: #0f0f1a;
    border: solid #0f3460;
}

#output-title {
    background: #16213e;
    color: #e94560;
    text-style: bold;
    padding: 0 1;
}

#output-log {
    background: transparent;
    padding: 1;
}
"""


def get_exercises_dir() -> Path:
    """Get the exercises directory."""
    return Path(__file__).parent.parent.parent / "exercises"


def run_tests(exercise_path: Path) -> tuple[str, str, int]:
    """Run pytest for an exercise."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(exercise_path), "-v", "--tb=short", "--no-header"],
            capture_output=True,
            text=True,
            timeout=60,
            cwd=exercise_path.parent.parent.parent,
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.TimeoutExpired:
        return "", "Test execution timed out!", 1
    except Exception as e:
        return "", f"Error: {e}", 1


class PytestBattleTUI(App):
    """Fast, simple TUI for pytest-battle."""

    TITLE = "Pytest Battle"
    CSS = SIMPLE_CSS

    BINDINGS: ClassVar[list[Binding]] = [
        Binding("q", "quit", "Quit"),
        Binding("r", "run_tests", "Run"),
        Binding("h", "show_hint", "Hint"),
        Binding("a", "run_all", "Run All"),
    ]

    def __init__(self):
        super().__init__()
        self.selected_path: Path | None = None
        self.selected_level: str = ""

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main-container"):
            with Vertical(id="sidebar"):
                yield Static("[ EXERCISES ]", id="sidebar-title")
                yield Tree("Levels", id="exercise-tree")

            with Vertical(id="content"):
                with Vertical(id="info-panel"):
                    yield Static("Selected: None", id="info-title")
                    yield Static("Select an exercise and press R to run tests", id="info-text")

                with Horizontal(id="button-bar"):
                    yield Button("Run [R]", id="btn-run", variant="primary")
                    yield Button("Hint [H]", id="btn-hint", variant="warning")
                    yield Button("Run All [A]", id="btn-all")

                with Vertical(id="output-panel"):
                    yield Static(" OUTPUT ", id="output-title")
                    yield RichLog(id="output-log", highlight=True, markup=True)

        yield Footer()

    def on_mount(self) -> None:
        """Build the exercise tree on mount."""
        self._build_tree()
        self._write_welcome()

    def _build_tree(self) -> None:
        """Build exercise tree without checking status (fast!)."""
        tree = self.query_one("#exercise-tree", Tree)
        tree.clear()
        tree.root.expand()

        exercises_dir = get_exercises_dir()
        levels = [
            ("01_junior", "Junior"),
            ("02_mid", "Mid"),
            ("03_senior", "Senior"),
        ]

        for dir_name, display_name in levels:
            level_path = exercises_dir / dir_name
            if not level_path.exists():
                continue

            level_node = tree.root.add(f"[bold cyan]{display_name}[/]", expand=True)
            level_node.data = {"type": "level", "path": level_path, "name": display_name.lower()}

            for ex_dir in sorted(level_path.iterdir()):
                if ex_dir.is_dir() and ex_dir.name.startswith("ex"):
                    # Format: "ex01_variables" -> "01. Variables"
                    parts = ex_dir.name.split("_", 1)
                    num = parts[0][2:]  # Remove "ex" prefix
                    name = parts[1].replace("_", " ").title() if len(parts) > 1 else ""
                    label = f"{num}. {name}"

                    ex_node = level_node.add_leaf(f"[ ] {label}")
                    ex_node.data = {
                        "type": "exercise",
                        "path": ex_dir,
                        "level": display_name.lower(),
                        "label": label,
                    }

    def _write_welcome(self) -> None:
        """Write welcome message."""
        log = self.query_one("#output-log", RichLog)
        log.write("[bold cyan]━━━ Pytest Battle ━━━[/]")
        log.write("")
        log.write("Select an exercise from the tree, then:")
        log.write("  [bold]R[/] - Run tests for selected exercise")
        log.write("  [bold]H[/] - Show hints")
        log.write("  [bold]A[/] - Run all exercises in selected level")
        log.write("  [bold]Q[/] - Quit")
        log.write("")
        log.write("[dim]Status is checked when you run tests.[/]")

    @on(Tree.NodeSelected)
    def on_tree_select(self, event: Tree.NodeSelected) -> None:
        """Handle exercise selection."""
        node = event.node
        if not node.data:
            return

        if node.data.get("type") == "exercise":
            self.selected_path = node.data["path"]
            self.selected_level = node.data["level"]

            title = self.query_one("#info-title", Static)
            text = self.query_one("#info-text", Static)

            title.update(f"Selected: {node.data['label']}")
            text.update(f"Level: {self.selected_level.upper()} | Press R to run tests")

        elif node.data.get("type") == "level":
            self.selected_path = node.data["path"]
            self.selected_level = node.data["name"]

            title = self.query_one("#info-title", Static)
            text = self.query_one("#info-text", Static)

            title.update(f"Level: {node.data['name'].upper()}")
            text.update("Press A to run all exercises in this level")

    @on(Button.Pressed, "#btn-run")
    def on_btn_run(self) -> None:
        self.action_run_tests()

    @on(Button.Pressed, "#btn-hint")
    def on_btn_hint(self) -> None:
        self.action_show_hint()

    @on(Button.Pressed, "#btn-all")
    def on_btn_all(self) -> None:
        self.action_run_all()

    def action_run_tests(self) -> None:
        """Run tests for selected exercise."""
        if not self.selected_path:
            log = self.query_one("#output-log", RichLog)
            log.write("[red]No exercise selected![/]")
            return

        if self.selected_path.is_dir() and not any(self.selected_path.glob("test_*.py")):
            # It's a level directory, not an exercise
            log = self.query_one("#output-log", RichLog)
            log.write("[yellow]Select a specific exercise, or press A to run all.[/]")
            return

        self._run_tests_async(self.selected_path)

    @work(exclusive=True, thread=True)
    def _run_tests_async(self, path: Path) -> None:
        """Run tests in background thread."""
        self.call_from_thread(self._log_running, path.name)

        stdout, stderr, code = run_tests(path)

        self.call_from_thread(self._log_results, stdout, stderr, code, path)

    def _log_running(self, name: str) -> None:
        """Show running message."""
        log = self.query_one("#output-log", RichLog)
        log.clear()
        log.write(f"[cyan]Running tests for {name}...[/]")
        log.write("")

    def _log_results(self, stdout: str, stderr: str, code: int, path: Path) -> None:
        """Show test results and update tree."""
        log = self.query_one("#output-log", RichLog)
        log.clear()

        if code == 0:
            log.write("[bold green]━━━ ALL TESTS PASSED ━━━[/]")
            status_mark = "[green][✓][/]"
        else:
            log.write("[bold red]━━━ TESTS FAILED ━━━[/]")
            status_mark = "[red][✗][/]"

        log.write("")

        # Color-code output
        for line in stdout.split("\n"):
            if not line.strip():
                continue
            if "PASSED" in line:
                log.write(f"[green]{line}[/]")
            elif "FAILED" in line:
                log.write(f"[red]{line}[/]")
            elif "ERROR" in line:
                log.write(f"[yellow]{line}[/]")
            elif line.startswith("="):
                log.write(f"[dim]{line}[/]")
            else:
                log.write(line)

        if stderr:
            log.write("")
            log.write(f"[yellow]{stderr}[/]")

        # Update tree node with status
        self._update_tree_status(path, status_mark)

    def _update_tree_status(self, path: Path, status: str) -> None:
        """Update the tree node label with pass/fail status."""
        tree = self.query_one("#exercise-tree", Tree)

        def update_node(node):
            if node.data and node.data.get("path") == path:
                label = node.data.get("label", path.name)
                node.set_label(f"{status} {label}")
                return True
            for child in node.children:
                if update_node(child):
                    return True
            return False

        update_node(tree.root)

    def action_show_hint(self) -> None:
        """Show hint for selected exercise."""
        log = self.query_one("#output-log", RichLog)

        if not self.selected_path or not self.selected_path.is_dir():
            log.write("[red]No exercise selected![/]")
            return

        # Find hint file
        hint_path = self.selected_path / "HINT.md"
        if not hint_path.exists():
            log.write("[yellow]No hint available for this exercise.[/]")
            return

        log.clear()
        log.write(f"[bold cyan]━━━ HINT: {self.selected_path.name} ━━━[/]")
        log.write("")

        content = hint_path.read_text()
        for line in content.split("\n"):
            if line.startswith("## "):
                log.write(f"[bold yellow]{line}[/]")
            elif line.startswith("# "):
                log.write(f"[bold cyan]{line}[/]")
            elif line.startswith("```"):
                log.write(f"[dim]{line}[/]")
            else:
                log.write(line)

    def action_run_all(self) -> None:
        """Run all exercises in the selected level."""
        if not self.selected_path:
            log = self.query_one("#output-log", RichLog)
            log.write("[red]No level selected![/]")
            return

        # Find the level directory
        if self.selected_path.name.startswith("ex"):
            level_dir = self.selected_path.parent
        else:
            level_dir = self.selected_path

        self._run_level_async(level_dir)

    @work(exclusive=True, thread=True)
    def _run_level_async(self, level_dir: Path) -> None:
        """Run all exercises in a level."""
        exercises = sorted([d for d in level_dir.iterdir() if d.is_dir() and d.name.startswith("ex")])

        self.call_from_thread(self._log_level_start, level_dir.name, len(exercises))

        passed = 0
        failed = 0

        for ex_path in exercises:
            self.call_from_thread(self._log_exercise_running, ex_path.name)

            stdout, stderr, code = run_tests(ex_path)

            if code == 0:
                passed += 1
                status = "[green][✓][/]"
                self.call_from_thread(self._log_exercise_result, ex_path.name, "PASSED", True)
            else:
                failed += 1
                status = "[red][✗][/]"
                self.call_from_thread(self._log_exercise_result, ex_path.name, "FAILED", False)

            self.call_from_thread(self._update_tree_status, ex_path, status)

        self.call_from_thread(self._log_level_summary, passed, failed)

    def _log_level_start(self, name: str, count: int) -> None:
        log = self.query_one("#output-log", RichLog)
        log.clear()
        log.write(f"[bold cyan]━━━ Running {count} exercises in {name} ━━━[/]")
        log.write("")

    def _log_exercise_running(self, name: str) -> None:
        log = self.query_one("#output-log", RichLog)
        log.write(f"[dim]Testing {name}...[/]")

    def _log_exercise_result(self, name: str, result: str, passed: bool) -> None:
        log = self.query_one("#output-log", RichLog)
        # Remove the "Testing..." line and add result
        color = "green" if passed else "red"
        log.write(f"[{color}]{name}: {result}[/]")

    def _log_level_summary(self, passed: int, failed: int) -> None:
        log = self.query_one("#output-log", RichLog)
        log.write("")
        log.write(f"[bold]━━━ Summary ━━━[/]")
        log.write(f"[green]Passed: {passed}[/]")
        log.write(f"[red]Failed: {failed}[/]")

        total = passed + failed
        pct = (passed / total * 100) if total > 0 else 0
        log.write(f"[cyan]Progress: {pct:.0f}%[/]")


def main() -> None:
    """Run the TUI."""
    app = PytestBattleTUI()
    app.run()


if __name__ == "__main__":
    main()
