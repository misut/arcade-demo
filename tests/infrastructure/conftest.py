from typing import TextIO
import os

from pytest import fixture

from paradox.infrastructure.repository import FileWorldRepository
from paradox.infrastructure.unit_of_work import FileWorldUnitOfWork


_WORLD_FILE_PATH = "tests/infrastructure/test_worlds.pkl"


@fixture(name="world_stream", scope="package")
def world_stream() -> TextIO:
    with open(_WORLD_FILE_PATH, "ab+") as stream:
        yield stream
    os.remove(_WORLD_FILE_PATH)


@fixture(name="world_repo", scope="package")
def world_repository(world_stream: TextIO) -> FileWorldRepository:
    return FileWorldRepository(world_stream)


@fixture(name="world_uow", scope="package")
def world_unit_of_work() -> FileWorldUnitOfWork:
    return FileWorldUnitOfWork(_WORLD_FILE_PATH)
