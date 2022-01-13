from arcade import View, Window
from arcade.gui import UIManager, UIOnClickEvent
from dependency_injector.wiring import Provide
import arcade

from paradox.domain.models import World
from paradox.infrastructure.repository import AbstractTextRepository
from paradox.infrastructure.unit_of_work import AbstractWorldUnitOfWork
from paradox.windows.containers import WorldEditContainer
from paradox.windows.worldedit.views.worldedit import WorldEditView


class NewWorldView(View):
    texts: AbstractTextRepository
    uis: UIManager
    uow: AbstractWorldUnitOfWork

    def __init__(
        self, 
        texts: AbstractTextRepository = Provide[WorldEditContainer.texts],
        uow: AbstractWorldUnitOfWork = Provide[WorldEditContainer.uow],
        window: Window = None,
    ) -> None:
        super().__init__(window)
        self.texts = texts
        self.uow = uow

        self.uis = UIManager(window)
        self.setup()
        
        new_world_box = arcade.gui.UIBoxLayout()

        world_name_input_text = arcade.gui.UIInputText(
            font_name=("Verdana"),
            text="Paradox",
            width=200,
        )
        new_world_box.add(world_name_input_text.with_space_around(bottom=20))

        create_world_button = arcade.gui.UIFlatButton(
            font_name=("Verdana"),
            text="hi",
            width=200,
        )
        @create_world_button.event("on_click")
        def on_click_create_world(event: UIOnClickEvent) -> None:
            world_name = world_name_input_text.text
            world = World(name=world_name)
            with self.uow as uow:
                uow.worlds.add(world)
                uow.commit()
            
            worldedit_view = WorldEditView(world=world, window=self.window)
            self.uis.disable()
            self.window.show_view(worldedit_view)
        new_world_box.add(create_world_button.with_space_around(bottom=20))

        self.uis.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=new_world_box,
            )
        )
        self.uis.enable()
    
    def setup(self) -> None:
        ...
    
    def on_draw(self) -> None:
        arcade.start_render()
        self.uis.draw()
