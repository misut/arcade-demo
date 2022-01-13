from arcade import Window
import arcade

from paradox.windows.containers import WorldEditContainer
from paradox.windows.settings import WorldEditSettings
from paradox.windows.worldedit import views


class WorldEditWindow(Window):
    container: WorldEditContainer
    settings: WorldEditSettings

    def __init__(self, settings: WorldEditSettings) -> None:
        self.container = WorldEditContainer()
        self.container.config.from_pydantic(settings)
        self.container.wire(packages=[views])
        self.settings = settings

        texts = self.container.texts.provided()
        super().__init__(
            width=settings.WINDOW_WIDTH,
            height=settings.WINDOW_HEIGHT,
            title=texts.get("window.title"),
            fullscreen=settings.FULLSCREEN,
            resizable=False,
        )
        self.setup()

    def setup(self) -> None:
        views.init_views(self)
        self.show_view(views.intro)

    def teardown(self) -> None:
        ...
