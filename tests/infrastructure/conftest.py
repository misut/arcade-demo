from pathlib import Path
import shutil

from pytest import fixture

from paradox.infrastructure.repository import FileWorldRepository
from paradox.infrastructure.unit_of_work import FileWorldUnitOfWork


_WORLD_PATH = Path("tests/infrastructure/worlds/")


@fixture(name="world_repo", scope="package")
def world_repository() -> FileWorldRepository:
    yield FileWorldRepository(world_path=_WORLD_PATH)

    if _WORLD_PATH.is_dir():
        shutil.rmtree(_WORLD_PATH)


@fixture(name="world_uow", scope="package")
def world_unit_of_work() -> FileWorldUnitOfWork:
    yield FileWorldUnitOfWork(world_path=_WORLD_PATH)
    
    if _WORLD_PATH.is_dir():
        shutil.rmtree(_WORLD_PATH)
