from paradox.domain.base import IVec3
from paradox.domain.models import Block, BlockType, World


def test_allocate_blocks() -> None:
    world = World(name="Hello, world!")
    
    coordinate = IVec3(1, 2, 3)
    expected_block = Block(coordinate=coordinate, type=BlockType.TEST)
    world.allocate_blocks(expected_block)

    assert world.at(coordinate) == expected_block
