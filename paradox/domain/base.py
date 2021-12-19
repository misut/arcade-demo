from __future__ import annotations

from abc import ABC
from typing import Tuple


class Vector(ABC):
    _tpl: Tuple

    def __eq__(self, other: Vector) -> bool:
        return all([x==y for x, y in zip(self._tpl, other._tpl)])

    def __hash__(self) -> int:
        return hash(self._tpl)

    def __str__(self) -> str:
        return "(" + ",".join(self._tpl) + ")"


class Vec2(Vector):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y
        self._tpl = (x, y)


class Vec3(Vector):
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z
        self._tpl = (x, y, z)


class IVec2(Vector):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self._tpl = (x, y)


class IVec3(Vector):
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x, self.y, self.z = x, y, z
        self._tpl = (x, y, z)
