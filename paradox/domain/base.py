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
        return "(" + ", ".join(map(str, self._tpl)) + ")"


class Vec2(Vector):
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y
        self._tpl = (x, y)
    
    def __add__(self, other: Vec2) -> Vec2:
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vec2) -> Vec2:
        return Vec2(self.x - other.x, self.y + other.y)


class Vec3(Vector):
    x: float
    y: float
    z: float

    def __init__(self, x: float, y: float, z: float) -> None:
        self.x, self.y, self.z = x, y, z
        self._tpl = (x, y, z)
    
    def __add__(self, other: Vec3) -> Vec3:
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vec3) -> Vec3:
        return Vec3(self.x - other.x, self.y + other.y, self.z - other.z)


class IVec2(Vector):
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x, self.y = x, y
        self._tpl = (x, y)
    
    def __add__(self, other: IVec2) -> IVec2:
        return IVec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: IVec2) -> IVec2:
        return IVec2(self.x - other.x, self.y + other.y)


class IVec3(Vector):
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int) -> None:
        self.x, self.y, self.z = x, y, z
        self._tpl = (x, y, z)
    
    def __add__(self, other: IVec3) -> IVec3:
        return IVec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: IVec3) -> IVec3:
        return IVec3(self.x - other.x, self.y + other.y, self.z - other.z)
