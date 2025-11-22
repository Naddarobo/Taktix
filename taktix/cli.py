#
# Taktix Game Module
#
import os

# Textual imports
from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Label, Button
from textual.containers import Container, Vertical, Horizontal

# Local imports
from taktix.screens.main_screen import MainMenuScreen
from taktix.screens.tutorial_screen import TutorialScreen
from taktix.screens.game_screen import GameScreen

class TaktixApp(App):
    """A Taktix game application."""
    
    CSS_PATH = "app.css"
    
    SCREENS = {
        "main_menu": MainMenuScreen,
        "tutorial": TutorialScreen,
        "game": GameScreen,
    }
    
    def on_mount(self) -> None:
        """Called when app starts."""
        self.push_screen("main_menu")

def main():
    app = TaktixApp()
    app.run()