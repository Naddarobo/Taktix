#
# Taktix Game Screen
#

from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Button
from textual.containers import Container, Vertical
from textual.app import ComposeResult


class GameScreen(Screen):
    """Game screen."""
    
    BINDINGS = [ ("escape", "menu", "Leave Game"), ("q", "quit", "Quit Game") ]
    
    def compose(self) -> ComposeResult:
        # yield Header()
        yield Container(
            Label("Game Screen", id="game-title"),
            Label("Game content goes here...", id="game-content"),
            Button("Back to Menu", id="back-btn"),
            id="game-container"
        )
        # yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle back button."""
        if event.button.id == "back-btn":
            self.app.pop_screen()
    
    # ===============================
    # region: Actions
    def action_menu(self) -> None:
        """Action to go back to menu."""
        self.app.pop_screen()

    def action_quit(self) -> None:
        """Action to quit the game."""
        self.app.exit()
    # endregion
    # ===============================