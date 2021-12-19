from paradox.domain.models import World
from paradox.infrastructure.unit_of_work import FileWorldUnitOfWork


def test_commit(world_uow: FileWorldUnitOfWork) -> None:
    world_name = "Hello, commit world!"
    expected_world = World(name=world_name)

    with world_uow as uow:
        uow.worlds.add(expected_world)
        uow.commit()
    
    with world_uow as uow:
        assert uow.worlds.get(world_name) == expected_world


def test_rollback(world_uow: FileWorldUnitOfWork) -> None:
    world_name = "Hello, rollback world!"
    world = World(name=world_name)

    with world_uow as uow:
        uow.worlds.add(world)
        uow.rollback()
    
    with world_uow as uow:
        assert uow.worlds.get(world_name) == None
