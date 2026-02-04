#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║  ⚙️  P Y T E S T - B A T T L E  ⚙️                                            ║
║     ═══════════════════════════                                               ║
║     A Steampunk-Powered Python Learning Engine                                ║
╚═══════════════════════════════════════════════════════════════════════════════╝

Steampunk TUI for pytest-battle - an interactive terminal interface
for learning Python through exercises.
"""

import subprocess
import sys
from pathlib import Path
from typing import ClassVar

from textual import on, work
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.reactive import reactive
from textual.widgets import (
    Button,
    Footer,
    Header,
    Label,
    ListItem,
    ListView,
    ProgressBar,
    RichLog,
    Rule,
    Static,
    Tree,
)
from textual.widgets.tree import TreeNode


# ══════════════════════════════════════════════════════════════════════════════
# STEAMPUNK ASCII ART & DECORATIONS
# ══════════════════════════════════════════════════════════════════════════════

GEAR_SMALL = """⚙"""

GEAR_LARGE = """
    ▄▄▄▄▄▄▄
  ▄█ ═══ █▄
 █ ╔═════╗ █
█══╣ ⚙⚙⚙ ╠══█
 █ ╚═════╝ █
  ▀█ ═══ █▀
    ▀▀▀▀▀▀▀
"""

BANNER = """
╔══════════════════════════════════════════════════════════════════════════════╗
║   ⚙️ ═══════════════════════════════════════════════════════════════════ ⚙️   ║
║   ║                                                                      ║   ║
║   ║   ██████╗ ██╗   ██╗████████╗███████╗███████╗████████╗               ║   ║
║   ║   ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝               ║   ║
║   ║   ██████╔╝ ╚████╔╝    ██║   █████╗  ███████╗   ██║                  ║   ║
║   ║   ██╔═══╝   ╚██╔╝     ██║   ██╔══╝  ╚════██║   ██║                  ║   ║
║   ║   ██║        ██║      ██║   ███████╗███████║   ██║                  ║   ║
║   ║   ╚═╝        ╚═╝      ╚═╝   ╚══════╝╚══════╝   ╚═╝                  ║   ║
║   ║                                                                      ║   ║
║   ║   ██████╗  █████╗ ████████╗████████╗██╗     ███████╗                ║   ║
║   ║   ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝                ║   ║
║   ║   ██████╔╝███████║   ██║      ██║   ██║     █████╗                  ║   ║
║   ║   ██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝                  ║   ║
║   ║   ██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗                ║   ║
║   ║   ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝                ║   ║
║   ║                                                                      ║   ║
║   ⚙️ ═══════════════════════════════════════════════════════════════════ ⚙️   ║
║                                                                              ║
║        ⚡ A Steam-Powered Python Learning Engine ⚡                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

MINI_BANNER = """⚙️ ══ PYTEST-BATTLE ══ ⚙️"""

LEVEL_ICONS = {
    "junior": "🔩",  # Bolt/screw for beginners
    "mid": "⚙️",      # Gear for intermediate
    "senior": "🔧",   # Wrench for advanced
}

STATUS_ICONS = {
    "passed": "✅",
    "failed": "❌",
    "pending": "⏳",
    "running": "🔄",
}


# ══════════════════════════════════════════════════════════════════════════════
# STEAMPUNK CSS THEME
# ══════════════════════════════════════════════════════════════════════════════

STEAMPUNK_CSS = """
/* ═══════════════════════════════════════════════════════════════════════════
   STEAMPUNK THEME - Brass, Copper, and Industrial Elegance
   ═══════════════════════════════════════════════════════════════════════════ */

$brass: #d4a84b;
$copper: #b87333;
$bronze: #cd7f32;
$rust: #8b4513;
$dark-metal: #2d2d2d;
$steam: #e8dcc4;
$coal: #1a1a1a;
$rivet: #8b7355;

Screen {
    background: $coal;
}

Header {
    background: $rust;
    color: $steam;
    text-style: bold;
    border-bottom: thick $brass;
}

Footer {
    background: $dark-metal;
    color: $brass;
    border-top: thick $copper;
}

/* ═══════════════════════════════════════════════════════════════════════════
   MAIN CONTAINERS
   ═══════════════════════════════════════════════════════════════════════════ */

#main-container {
    layout: horizontal;
    height: 100%;
}

#sidebar {
    width: 40;
    border-right: thick $brass;
    background: $dark-metal;
}

#content {
    width: 1fr;
    background: $coal;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PANELS
   ═══════════════════════════════════════════════════════════════════════════ */

.panel {
    border: thick $copper;
    background: $dark-metal;
    margin: 1;
    padding: 1;
}

.panel-title {
    text-align: center;
    text-style: bold;
    color: $brass;
    background: $rust;
    padding: 1;
    margin-bottom: 1;
    border: solid $copper;
}

/* ═══════════════════════════════════════════════════════════════════════════
   EXERCISE TREE
   ═══════════════════════════════════════════════════════════════════════════ */

#exercise-tree {
    background: $dark-metal;
    scrollbar-color: $brass;
    scrollbar-color-hover: $copper;
    scrollbar-color-active: $bronze;
}

Tree {
    background: transparent;
    padding: 1;
}

Tree > .tree--guides {
    color: $rivet;
}

Tree > .tree--cursor {
    background: $rust;
    color: $steam;
    text-style: bold;
}

Tree > .tree--highlight {
    background: $copper 30%;
}

TreeNode {
    color: $steam;
}

TreeNode:hover {
    background: $copper 20%;
}

/* ═══════════════════════════════════════════════════════════════════════════
   PROGRESS SECTION
   ═══════════════════════════════════════════════════════════════════════════ */

#progress-section {
    height: auto;
    max-height: 12;
    border: thick $copper;
    background: $dark-metal;
    margin: 1;
    padding: 1;
}

#progress-title {
    text-align: center;
    text-style: bold;
    color: $brass;
    margin-bottom: 1;
}

.progress-row {
    height: 3;
    margin-bottom: 1;
}

.progress-label {
    width: 15;
    color: $steam;
}

ProgressBar {
    width: 1fr;
    padding-right: 1;
}

ProgressBar > .bar--bar {
    color: $brass;
    background: $coal;
}

ProgressBar > .bar--complete {
    color: $bronze;
}

#progress-text {
    text-align: center;
    color: $copper;
    text-style: italic;
    margin-top: 1;
}

/* ═══════════════════════════════════════════════════════════════════════════
   TEST OUTPUT LOG
   ═══════════════════════════════════════════════════════════════════════════ */

#output-section {
    height: 1fr;
    border: thick $copper;
    background: $dark-metal;
    margin: 1;
}

#output-title {
    text-align: center;
    text-style: bold;
    color: $brass;
    background: $rust;
    padding: 1;
    border-bottom: solid $copper;
}

#test-output {
    background: $coal;
    color: $steam;
    padding: 1;
    scrollbar-color: $brass;
    scrollbar-color-hover: $copper;
}

RichLog {
    background: transparent;
}

/* ═══════════════════════════════════════════════════════════════════════════
   EXERCISE INFO PANEL
   ═══════════════════════════════════════════════════════════════════════════ */

#info-section {
    height: auto;
    max-height: 15;
    border: thick $copper;
    background: $dark-metal;
    margin: 1;
    padding: 1;
}

#info-title {
    text-align: center;
    text-style: bold;
    color: $brass;
    margin-bottom: 1;
}

#info-content {
    color: $steam;
    padding: 1;
}

.info-label {
    color: $copper;
    text-style: bold;
}

.info-value {
    color: $steam;
}

/* ═══════════════════════════════════════════════════════════════════════════
   BUTTONS
   ═══════════════════════════════════════════════════════════════════════════ */

Button {
    background: $rust;
    color: $steam;
    border: tall $brass;
    margin: 1;
    min-width: 16;
}

Button:hover {
    background: $copper;
    border: tall $bronze;
}

Button:focus {
    background: $bronze;
    border: tall $brass;
    text-style: bold;
}

Button.-primary {
    background: $copper;
}

Button.-success {
    background: #2e7d32;
}

Button.-warning {
    background: $rust;
}

#button-bar {
    height: auto;
    align: center middle;
    margin: 1;
}

/* ═══════════════════════════════════════════════════════════════════════════
   STATUS INDICATORS
   ═══════════════════════════════════════════════════════════════════════════ */

.status-passed {
    color: #4caf50;
    text-style: bold;
}

.status-failed {
    color: #f44336;
    text-style: bold;
}

.status-pending {
    color: $brass;
}

.status-running {
    color: $copper;
    text-style: italic;
}

/* ═══════════════════════════════════════════════════════════════════════════
   DECORATIVE ELEMENTS
   ═══════════════════════════════════════════════════════════════════════════ */

.gear-decoration {
    color: $brass;
    text-align: center;
}

.divider {
    color: $copper;
    margin: 1 0;
}

Rule {
    color: $copper;
    margin: 1 0;
}

/* ═══════════════════════════════════════════════════════════════════════════
   WELCOME SCREEN
   ═══════════════════════════════════════════════════════════════════════════ */

#welcome-container {
    align: center middle;
    width: 100%;
    height: 100%;
}

#welcome-banner {
    color: $brass;
    text-align: center;
    padding: 2;
}

#welcome-subtitle {
    color: $copper;
    text-align: center;
    text-style: italic;
    margin-top: 2;
}

/* ═══════════════════════════════════════════════════════════════════════════
   LOADING INDICATOR
   ═══════════════════════════════════════════════════════════════════════════ */

.loading {
    color: $brass;
    text-style: italic;
}

.spinning-gear {
    color: $copper;
}
"""


# ══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def get_exercises_dir() -> Path:
    """Get the exercises directory."""
    return Path(__file__).parent.parent.parent / "exercises"


# ══════════════════════════════════════════════════════════════════════════════
# STATUS CACHE - prevents duplicate subprocess calls
# ══════════════════════════════════════════════════════════════════════════════

_status_cache: dict[str, tuple[str, float]] = {}  # path -> (status, mtime)


def _get_exercise_mtime(exercise_path: Path) -> float:
    """Get the latest modification time of exercise files."""
    try:
        mtimes = []
        for f in exercise_path.glob("*.py"):
            mtimes.append(f.stat().st_mtime)
        return max(mtimes) if mtimes else 0.0
    except Exception:
        return 0.0


def clear_status_cache() -> None:
    """Clear the status cache."""
    _status_cache.clear()


def get_exercise_status(exercise_path: Path, use_cache: bool = True) -> str:
    """Run tests for an exercise and return status.

    Args:
        exercise_path: Path to the exercise directory
        use_cache: If True, use cached status if files haven't changed
    """
    cache_key = str(exercise_path)
    current_mtime = _get_exercise_mtime(exercise_path)

    # Check cache first
    if use_cache and cache_key in _status_cache:
        cached_status, cached_mtime = _status_cache[cache_key]
        if cached_mtime >= current_mtime:
            return cached_status

    # Run tests
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(exercise_path), "-q", "--tb=no"],
            capture_output=True,
            timeout=30,
            cwd=exercise_path.parent.parent.parent,
        )
        status = "passed" if result.returncode == 0 else "failed"
    except subprocess.TimeoutExpired as e:
        # Kill the child process to prevent zombies
        if e.args and hasattr(e, 'child'):
            try:
                e.child.kill()
                e.child.wait()
            except Exception:
                pass
        status = "failed"
    except Exception:
        status = "failed"

    # Update cache
    _status_cache[cache_key] = (status, current_mtime)
    return status


def run_exercise_tests(exercise_path: Path) -> tuple[str, str, int]:
    """Run tests for an exercise and return (stdout, stderr, returncode)."""
    process = None
    try:
        process = subprocess.Popen(
            [sys.executable, "-m", "pytest", str(exercise_path), "-v", "--tb=short"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd=exercise_path.parent.parent.parent,
        )
        stdout, stderr = process.communicate(timeout=60)
        returncode = process.returncode

        # Invalidate cache since we ran tests (file might have changed)
        cache_key = str(exercise_path)
        if cache_key in _status_cache:
            del _status_cache[cache_key]

        return stdout, stderr, returncode
    except subprocess.TimeoutExpired:
        # Kill the process and its children
        if process:
            try:
                process.kill()
                process.wait(timeout=5)
            except Exception:
                pass
        return "", "⚠️ Test execution timed out!", 1
    except Exception as e:
        if process:
            try:
                process.kill()
                process.wait(timeout=5)
            except Exception:
                pass
        return "", f"⚠️ Error running tests: {e}", 1


def count_exercises(use_cache: bool = True) -> dict[str, tuple[int, int]]:
    """Count passed/total exercises per level.

    Args:
        use_cache: If True, use cached status (much faster after populate_tree)
    """
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
                # Use cache to avoid duplicate subprocess calls
                if get_exercise_status(ex_dir, use_cache=use_cache) == "passed":
                    passed += 1

        counts[level_name] = (passed, total)

    return counts


# ══════════════════════════════════════════════════════════════════════════════
# CUSTOM WIDGETS
# ══════════════════════════════════════════════════════════════════════════════

class GearDecoration(Static):
    """A decorative gear widget."""

    def __init__(self, size: str = "small", **kwargs):
        super().__init__(**kwargs)
        self.gear_size = size

    def compose(self) -> ComposeResult:
        if self.gear_size == "large":
            yield Static(GEAR_LARGE, classes="gear-decoration")
        else:
            yield Static("⚙️", classes="gear-decoration")


class SteampunkProgressBar(Static):
    """A steampunk-styled progress indicator."""

    progress = reactive(0.0)
    label = reactive("")

    def __init__(self, label: str = "", **kwargs):
        super().__init__(**kwargs)
        self.label = label

    def compose(self) -> ComposeResult:
        with Horizontal(classes="progress-row"):
            yield Label(f"{self.label}:", classes="progress-label")
            yield ProgressBar(total=100, show_eta=False)

    def watch_progress(self, value: float) -> None:
        """Update progress bar when progress changes."""
        bar = self.query_one(ProgressBar)
        bar.update(progress=value)


class ExerciseInfo(Static):
    """Display information about selected exercise."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exercise_name = ""
        self.exercise_level = ""
        self.exercise_status = "pending"

    def compose(self) -> ComposeResult:
        yield Static("⚙️ ═══ EXERCISE INFO ═══ ⚙️", id="info-title")
        yield Static("Select an exercise to view details", id="info-content")

    def update_info(self, name: str, level: str, status: str, description: str = ""):
        """Update the exercise information display."""
        self.exercise_name = name
        self.exercise_level = level
        self.exercise_status = status

        level_icon = LEVEL_ICONS.get(level, "⚙️")
        status_icon = STATUS_ICONS.get(status, "⏳")

        content = f"""
[bold]{level_icon} {name}[/bold]

[dim]Level:[/dim] {level.upper()}
[dim]Status:[/dim] {status_icon} {status.upper()}

{description}
        """.strip()

        self.query_one("#info-content", Static).update(content)


# ══════════════════════════════════════════════════════════════════════════════
# MAIN TUI APPLICATION
# ══════════════════════════════════════════════════════════════════════════════

class PytestBattleTUI(App):
    """The main Pytest Battle TUI application."""

    TITLE = "⚙️ Pytest Battle ⚙️"
    SUB_TITLE = "Steam-Powered Python Learning"
    CSS = STEAMPUNK_CSS

    BINDINGS: ClassVar[list[Binding]] = [
        Binding("q", "quit", "Quit", show=True),
        Binding("r", "run_tests", "Run Tests", show=True),
        Binding("h", "show_hint", "Show Hint", show=True),
        Binding("f", "refresh", "Refresh", show=True),
        Binding("escape", "go_back", "Back", show=False),
    ]

    selected_exercise: reactive[Path | None] = reactive(None)

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main-container"):
            # Left sidebar with exercise tree
            with Vertical(id="sidebar"):
                yield Static("⚙️ ═══ EXERCISES ═══ ⚙️", classes="panel-title")
                yield Tree("📚 Levels", id="exercise-tree")

            # Right content area
            with Vertical(id="content"):
                # Progress section
                with Vertical(id="progress-section"):
                    yield Static("⚙️ ═══ STEAM PRESSURE GAUGES ═══ ⚙️", id="progress-title")
                    yield SteampunkProgressBar(label="🔩 Junior", id="junior-progress")
                    yield SteampunkProgressBar(label="⚙️  Mid", id="mid-progress")
                    yield SteampunkProgressBar(label="🔧 Senior", id="senior-progress")
                    yield Static("", id="progress-text")

                # Button bar
                with Horizontal(id="button-bar"):
                    yield Button("▶️ Run Tests", id="run-btn", variant="primary")
                    yield Button("💡 Hint", id="hint-btn", variant="warning")
                    yield Button("🔄 Refresh", id="refresh-btn")

                # Exercise info
                with Vertical(id="info-section"):
                    yield ExerciseInfo(id="exercise-info")

                # Test output
                with Vertical(id="output-section"):
                    yield Static("⚙️ ═══ STEAM CONSOLE OUTPUT ═══ ⚙️", id="output-title")
                    yield RichLog(id="test-output", highlight=True, markup=True)

        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app when mounted."""
        self.write_welcome_message()
        self._show_loading_message()
        # Load exercises asynchronously to prevent UI blocking
        self.load_exercises_async()

    def write_welcome_message(self) -> None:
        """Write welcome message to output."""
        output = self.query_one("#test-output", RichLog)
        output.write("[bold #d4a84b]" + "═" * 60 + "[/]")
        output.write("[bold #d4a84b]⚙️  Welcome to Pytest Battle! ⚙️[/]")
        output.write("[bold #d4a84b]" + "═" * 60 + "[/]")
        output.write("")
        output.write("[#e8dcc4]Select an exercise from the tree on the left,[/]")
        output.write("[#e8dcc4]then press [bold]R[/] or click [bold]Run Tests[/] to test your solution.[/]")
        output.write("")
        output.write("[#b87333]Press [bold]H[/] for hints when you're stuck.[/]")
        output.write("[#b87333]Press [bold]Q[/] to quit.[/]")
        output.write("")
        output.write("[dim #8b7355]May your gears turn smoothly! 🔧[/]")
        output.write("")

    def _show_loading_message(self) -> None:
        """Show loading indicator in the progress section."""
        progress_text = self.query_one("#progress-text", Static)
        progress_text.update("[bold #d4a84b]⚙️ Loading exercises... ⚙️[/]")

    @work(exclusive=True, thread=True)
    def load_exercises_async(self) -> None:
        """Load exercises in a background thread to prevent UI blocking."""
        # Collect exercise data in background thread
        exercises_dir = get_exercises_dir()
        exercise_data = []

        level_names = {
            "01_junior": ("🔩 Junior", "junior"),
            "02_mid": ("⚙️  Mid", "mid"),
            "03_senior": ("🔧 Senior", "senior"),
        }

        for level_dir in sorted(exercises_dir.iterdir()):
            if not level_dir.is_dir():
                continue

            display_name, level_key = level_names.get(
                level_dir.name,
                (level_dir.name, "unknown")
            )
            level_data = {
                "display_name": display_name,
                "level_key": level_key,
                "path": level_dir,
                "exercises": [],
            }

            for ex_dir in sorted(level_dir.iterdir()):
                if not ex_dir.is_dir() or not ex_dir.name.startswith("ex"):
                    continue

                # Get status (this populates the cache)
                status = get_exercise_status(ex_dir)
                level_data["exercises"].append({
                    "path": ex_dir,
                    "status": status,
                    "level_key": level_key,
                })

            exercise_data.append(level_data)

        # Update UI on main thread
        self.call_from_thread(self._populate_tree_from_data, exercise_data)
        self.call_from_thread(self.update_progress)

    def _populate_tree_from_data(self, exercise_data: list) -> None:
        """Populate tree from pre-loaded data (runs on main thread)."""
        tree = self.query_one("#exercise-tree", Tree)
        tree.clear()
        tree.root.expand()

        for level_data in exercise_data:
            level_node = tree.root.add(f"[bold]{level_data['display_name']}[/]", expand=True)
            level_node.data = {"type": "level", "path": level_data["path"]}

            for ex_data in level_data["exercises"]:
                status = ex_data["status"]
                status_icon = STATUS_ICONS.get(status, "⏳")
                ex_name = ex_data["path"].name.replace("_", " ").title()

                if status == "passed":
                    label = f"[green]{status_icon} {ex_name}[/]"
                else:
                    label = f"[#e8dcc4]{status_icon} {ex_name}[/]"

                ex_node = level_node.add_leaf(label)
                ex_node.data = {
                    "type": "exercise",
                    "path": ex_data["path"],
                    "level": ex_data["level_key"],
                    "status": status,
                }

    def populate_tree(self) -> None:
        """Populate the exercise tree."""
        tree = self.query_one("#exercise-tree", Tree)
        tree.clear()
        tree.root.expand()

        exercises_dir = get_exercises_dir()

        level_names = {
            "01_junior": ("🔩 Junior", "junior"),
            "02_mid": ("⚙️  Mid", "mid"),
            "03_senior": ("🔧 Senior", "senior"),
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
                status_icon = STATUS_ICONS.get(status, "⏳")

                # Format exercise name
                ex_name = ex_dir.name.replace("_", " ").title()

                if status == "passed":
                    label = f"[green]{status_icon} {ex_name}[/]"
                else:
                    label = f"[#e8dcc4]{status_icon} {ex_name}[/]"

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
                widget_id = f"#{level}-progress"
                progress_widget = self.query_one(widget_id, SteampunkProgressBar)
                progress_widget.progress = progress_pct
            except Exception:
                pass

        # Update overall progress text
        overall_pct = (total_passed / total_exercises * 100) if total_exercises > 0 else 0
        progress_text = self.query_one("#progress-text", Static)
        progress_text.update(
            f"[bold #d4a84b]⚡ Overall: {total_passed}/{total_exercises} ({overall_pct:.0f}%) ⚡[/]"
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
            output.write("[bold #f44336]⚠️ No exercise selected![/]")
            output.write("[#e8dcc4]Select an exercise from the tree first.[/]")
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

        # Refresh progress and tree using async loading (prevents UI blocking)
        self.call_from_thread(self.load_exercises_async)

    def _show_running(self, name: str) -> None:
        """Show running status in output."""
        output = self.query_one("#test-output", RichLog)
        output.clear()
        output.write(f"[bold #d4a84b]⚙️ ═══ Running tests for {name} ═══ ⚙️[/]")
        output.write("")
        output.write("[#b87333]🔄 Steam engines warming up...[/]")
        output.write("")

    def _show_results(self, stdout: str, stderr: str, returncode: int) -> None:
        """Show test results in output."""
        output = self.query_one("#test-output", RichLog)
        output.clear()

        if returncode == 0:
            output.write("[bold #4caf50]" + "═" * 50 + "[/]")
            output.write("[bold #4caf50]✅ ALL TESTS PASSED! ⚙️[/]")
            output.write("[bold #4caf50]" + "═" * 50 + "[/]")
        else:
            output.write("[bold #f44336]" + "═" * 50 + "[/]")
            output.write("[bold #f44336]❌ SOME TESTS FAILED[/]")
            output.write("[bold #f44336]" + "═" * 50 + "[/]")

        output.write("")

        if stdout:
            for line in stdout.split("\n"):
                # Color code the output
                if "PASSED" in line:
                    output.write(f"[#4caf50]{line}[/]")
                elif "FAILED" in line:
                    output.write(f"[#f44336]{line}[/]")
                elif "ERROR" in line:
                    output.write(f"[#ff9800]{line}[/]")
                elif line.startswith("="):
                    output.write(f"[#d4a84b]{line}[/]")
                else:
                    output.write(f"[#e8dcc4]{line}[/]")

        if stderr:
            output.write("")
            output.write("[bold #ff9800]⚠️ Errors:[/]")
            output.write(f"[#ff9800]{stderr}[/]")

    def action_show_hint(self) -> None:
        """Show hint for selected exercise."""
        if not self.selected_exercise:
            output = self.query_one("#test-output", RichLog)
            output.write("[bold #f44336]⚠️ No exercise selected![/]")
            return

        hint_path = self.selected_exercise / "HINT.md"
        output = self.query_one("#test-output", RichLog)
        output.clear()

        if hint_path.exists():
            output.write("[bold #d4a84b]" + "═" * 50 + "[/]")
            output.write(f"[bold #d4a84b]💡 HINT for {self.selected_exercise.name}[/]")
            output.write("[bold #d4a84b]" + "═" * 50 + "[/]")
            output.write("")

            content = hint_path.read_text()
            for line in content.split("\n"):
                if line.startswith("#"):
                    output.write(f"[bold #b87333]{line}[/]")
                elif line.startswith("```"):
                    output.write(f"[#8b7355]{line}[/]")
                else:
                    output.write(f"[#e8dcc4]{line}[/]")
        else:
            output.write("[#f44336]No hint available for this exercise.[/]")

    def action_refresh(self) -> None:
        """Refresh the exercise tree and progress."""
        output = self.query_one("#test-output", RichLog)
        output.clear()
        output.write("[#d4a84b]🔄 Refreshing...[/]")

        # Clear cache to force re-checking all exercises
        clear_status_cache()
        self._show_loading_message()

        # Use async loading to prevent UI blocking
        self.load_exercises_async()

    def action_go_back(self) -> None:
        """Clear selection."""
        self.selected_exercise = None


# ══════════════════════════════════════════════════════════════════════════════
# ENTRY POINT
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    """Run the Pytest Battle TUI."""
    app = PytestBattleTUI()
    app.run()


if __name__ == "__main__":
    main()
