from paradox.domain.models import World
from paradox.infrastructure.repository import FileWorldRepository


def test_world_add_and_get(world_repo: FileWorldRepository) -> None:
    world_name = "Hello, addition world!"
    expected_world = World(name=world_name)

    world_repo.add(expected_world)
    assert world_repo.get(world_name) == expected_world


def test_world_remove_and_get(world_repo: FileWorldRepository) -> None:
    world_name = "Hello, removal world!"
    world = World(name=world_name)

    world_repo.add(world)
    world_repo.remove(world_name)
    assert world_repo.get(world_name) == None
