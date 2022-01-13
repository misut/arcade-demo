from enum import Enum, unique
from typing import Any, Dict, Optional

from arcade import Sprite, SpriteList
from pydantic import BaseModel, Field

from paradox.domain.base import IVec3, Vec2, Vec3


@unique
class BlockType(str, Enum):
    TEST = "test"
    GRASS = "grass"


class Block(BaseModel):
    coordinate: IVec3
    type: BlockType

    size: IVec3 = Field(default=IVec3(1, 1, 1))
    sprites: SpriteList = Field(default_factory=SpriteList)

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)


class World(BaseModel):
    name: str

    chunk: Dict[IVec3, Block] = Field(default={})
    sprites: SpriteList = Field(default=SpriteList())

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)

    def allocate_blocks(self, *blocks: Block) -> None:
        for block in blocks:
            if not self.can_allocate_block(block):
                continue
            self.chunk[block.coordinate] = block

    def at(self, coordinate: IVec3) -> Optional[Block]:
        return self.chunk.get(coordinate, None)

    def can_allocate_block(self, block: Block) -> bool:
        return self.chunk.get(block.coordinate, None) is None

    def draw(self, center: IVec3) -> None:
        ...
