from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer
from textual.widgets import Button, Digits, Header, Footer
from textual import events

class StopwatchApp(App):
    CSS_PATH = "stopwatch.tcss"
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def __init__(self):
        super().__init__()
        self.elapsed = 0.0
        self.running = False
        self._timer = None
    
    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical(id="wrap"):
            with Horizontal(id="controls"):
                yield Button("Start", id="start", variant="success")
                yield Button("Stop", id="stop", variant="error", disabled=True)
                yield Button("Reset", id="reset")
            yield Digits("00:00:00.00", id="display")
        yield Footer()

    async def on_mount(self) -> None:
        # Timer tick each 0.01 seconds
        self._timer = self.set_interval(0.01, self._on_tick, pause=True)

    def _format(self, t: float) -> str:
        # Format HH:MM::SS.ss
        hours = int(t // 3600)
        minutes = int((t % 3600) // 60)
        seconds = int(t % 60)
        hundredths = int((t - int(t)) * 100)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{hundredths:02d}"

    def _update_display(self) -> None:
        display = self.query_one("#display", Digits)
        display.update(self._format(self.elapsed))

    def _on_tick(self) -> None:
        if self.running:
            self.elapsed += 0.01
            self._update_display()

    def action_toggle_dark(self) -> None:
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def action_reset(self) -> None:
        self.elapsed = 0.0
        self._update_display()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "start":
            self.running = True
            self._timer.resume()
            self.query_one("#start", Button).disabled = True
            self.query_one("#stop", Button).disabled = False

        elif event.button.id == "stop":
            self.running = False
            self._timer.pause()
            self.query_one("#start", Button).disabled = False
            self.query_one("#stop", Button).disabled = True

        elif event.button.id == "reset":
            self.action_reset()
        
if __name__ == "__main__":
    StopwatchApp().run()