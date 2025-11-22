#
# Taktix Tutorial Screen
#

from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Button
from textual.containers import Container, Vertical
from textual.app import ComposeResult

class TutorialScreen(Screen):
    """Tutorial screen."""
    
    BINDINGS = [("escape", "back", "Back")]
    
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Tutorial", id="tutorial-title"),
            Label("Welcome to Taktix! This is the tutorial screen.", id="tutorial-content"),
            Button("Back to Menu", id="back-btn"),
            id="tutorial-container"
        )
        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle back button."""
        if event.button.id == "back-btn":
            self.app.pop_screen()
    
    def action_back(self) -> None:
        """Action to go back."""
        self.app.pop_screen()