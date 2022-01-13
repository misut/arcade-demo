from typing import List, Optional

from arcade import Camera, Scene, View, Window
from arcade.gui import UIManager
import arcade

from paradox.domain.base import Vec2, Vec3
from paradox.domain.models import World


def project(
    coordinate: Vec3,
    anchor: Vec3 = Vec3(0.0, 0.0, 0.0),
    window_width: int = 1280,
    window_height: int = 720,
    window_scale: float = 2.0
) -> Vec2:
    projected = Vec2(window_width / 2.0, window_height / 2.0)
    delta = coordinate - anchor
    projected.x += (delta.x - delta.y) * 30.0 * window_scale
    projected.y += (2 * delta.z - delta.x - delta.y) * 15.0 * window_scale
    return projected


class WorldScene(Scene):
    world: World

    def __init__(self, world: World) -> None:
        super().__init__()
        self.world = world

    def on_update(self, delta_time: float = 1 / 60, names: Optional[List[str]] = None) -> None:
        return super().on_update(delta_time=delta_time, names=names)


class WorldEditView(View):
    camera: Camera
    scene: WorldScene
    uis: UIManager
    world: World

    def __init__(self, world: World, window: Window = None) -> None:
        super().__init__(window=window)
        self.world = world

        self.uis = UIManager()

        self.uis.enable()

    def setup(self) -> None:
        self.camera = Camera(self.window)
        self.scene = WorldScene(self.world)

    def on_draw(self) -> None:
        arcade.start_render()
        self.scene.draw()
        