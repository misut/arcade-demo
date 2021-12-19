from enum import Enum, unique
from typing import Dict, Optional

from pydantic import BaseModel, Field

from paradox.domain.base import IVec3


@unique
class BlockType(str, Enum):
    TEST = "test"


class Block(BaseModel):
    coordinate: IVec3
    type: BlockType

    size: IVec3 = Field(default=IVec3(1, 1, 1))

    class Config:
        arbitrary_types_allowed = True


class World(BaseModel):
    name: str
    chunk: Dict[IVec3, Block] = Field(default={})

    def add_blocks(self, *blocks: Block) -> None:
        for block in blocks:
            self.chunk[block.coordinate] = block

    def at(self, coordinate: IVec3) -> Optional[Block]:
        return self.chunk.get(coordinate, None)

    class Config:
        arbitrary_types_allowed = True
