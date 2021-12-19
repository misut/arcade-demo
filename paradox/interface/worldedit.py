import arcade

from paradox.interface.containers import WorldEditContainer
from paradox.interface.settings import WorldEditSettings


class WorldEditWindow(arcade.Window):
    container: WorldEditContainer

    def __init__(self, settings: WorldEditSettings) -> None:
        self.container = WorldEditContainer()
        self.container.config.from_pydantic(settings)

    def setup(self) -> None:
        ...

    def teardown(self) -> None:
        ...

    def on_draw(self):
        return super().on_draw()

    def on_update(self, delta_time: float):
        return super().on_update(delta_time)
    
    def on_key_press(self, symbol: int, modifiers: int):
        return super().on_key_press(symbol, modifiers)
    
    def on_key_release(self, symbol: int, modifiers: int):
        return super().on_key_release(symbol, modifiers)
