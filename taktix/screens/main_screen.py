#
# Taktix Main Menu Screen
#

from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Button
from textual.containers import Container, Vertical
from textual.app import ComposeResult

class MainMenuScreen(Screen):
    """Main menu screen."""
    
    def compose(self) -> ComposeResult:
        # yield Header()
        yield Container(
            Vertical(
                Label("Taktix", id="title"),
                Button("Play Game", id="play-btn", variant="primary"),
                Button("Tutorial", id="tutorial-btn"),
                Button("Quit", id="quit-btn", variant="error"),
                id="menu-container"
            ),
            id="main-container"
        )
        # yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "play-btn":
            self.app.push_screen("game")
        elif event.button.id == "tutorial-btn":
            self.app.push_screen("tutorial")
        elif event.button.id == "quit-btn":
            self.app.exit()