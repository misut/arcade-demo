from typing import Dict
from arcade import Camera, View, Window
from arcade.gui import UIManager, UIOnClickEvent
from dependency_injector.wiring import Provide
import arcade

from paradox.domain.models import World
from paradox.infrastructure.repository import AbstractTextRepository
from paradox.infrastructure.unit_of_work import AbstractWorldUnitOfWork
from paradox.windows.containers import WorldEditContainer
from paradox.windows.worldedit.views.new_world import NewWorldView
from paradox.windows.worldedit.views.worldedit import WorldEditView


class IntroView(View):
    camera: Camera
    texts: AbstractTextRepository
    uis: UIManager
    uow: AbstractWorldUnitOfWork
    worlds: Dict[str, World]

    def __init__(
        self,
        texts: AbstractTextRepository = Provide[WorldEditContainer.texts],
        uow: AbstractWorldUnitOfWork = Provide[WorldEditContainer.uow],
        window: Window = None
    ) -> None:
        super().__init__(window)
        self.texts = texts
        self.uow = uow

        self.camera = Camera(window=window)
        self.uis = UIManager(window)
        self.setup()

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        world_box = arcade.gui.UIBoxLayout()

        for world_name, world in self.worlds.items():
            world_button = arcade.gui.UIFlatButton(
                font_name="Verdana",
                text=world_name,
                width=200,
            )
            @world_button.event("on_click")
            def on_click_world(event: UIOnClickEvent) -> None:
                world_view = WorldEditView(world=world, window=self.window)
                self.uis.disable()
                self.window.show_view(world_view)
            world_box.add(world_button.with_space_around(bottom=20))

        new_world_button = arcade.gui.UIFlatButton(
            font_name="Verdana",
            text=self.texts.get("button.new_world"),
            width=200,
        )
        @new_world_button.event("on_click")
        def on_click_new_world(event) -> None:
            new_world_view = NewWorldView(window=self.window)
            self.uis.disable()
            self.window.show_view(new_world_view)
        world_box.add(new_world_button.with_space_around(bottom=20))

        quit_button = arcade.gui.UIFlatButton(
            font_name="Verdana",
            text=self.texts.get("button.quit"),
            width=200,
        )
        @quit_button.event("on_click")
        def on_click_quit(event) -> None:
            arcade.exit()
        world_box.add(quit_button.with_space_around(bottom=20))
        
        self.uis.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=world_box,
            )
        )

        self.uis.enable()

    def setup(self) -> None:
        with self.uow as uow:
            self.worlds = uow.worlds.mapping

    def on_draw(self) -> None:
        arcade.start_render()
        # self.camera.use()
        self.uis.draw()
