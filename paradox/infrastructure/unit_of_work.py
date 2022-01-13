from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
import os
import pickle
import shutil

from paradox.infrastructure.repository import (
    AbstractWorldRepository,
    FileWorldRepository,
)


class AbstractWorldUnitOfWork(ABC):
    worlds: AbstractWorldRepository

    def __enter__(self) -> AbstractWorldUnitOfWork:
        return self
    
    def __exit__(self, *args: Any) -> None:
        ...

    @abstractmethod
    def commit(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def rollback(self) -> None:
        raise NotImplementedError


class FileWorldUnitOfWork(AbstractWorldUnitOfWork):
    world_path: Path

    def __init__(self, world_path: Path) -> None:
        self.world_path = world_path
    
    def __enter__(self) -> FileWorldUnitOfWork:
        self.world_path.mkdir(parents=True, exist_ok=True)
        for file_path in self.world_path.iterdir():
            if not (file_path.is_file() and file_path.suffix == ".pkl"):
                continue
            shutil.copyfile(
                src=file_path,
                dst=file_path.with_suffix(".backup")
            )
        self.worlds = FileWorldRepository(world_path=self.world_path)
        return super().__enter__()

    def __exit__(self, *args: Any) -> None:
        super().__exit__(*args)

        # Remove backup files
        for file_path in self.world_path.iterdir():
            if not file_path.is_file():
                continue
            if file_path.suffix == ".backup":
                os.remove(file_path)

    def commit(self) -> None:
        # Pickle worlds
        for world_name, world in self.worlds.mapping.items():
            file_path = self.world_path.joinpath(f"{world_name}.pkl")
            file_path.touch(exist_ok=True)
            with file_path.open("rb+") as stream:
                pickle.dump(world, stream)

    def rollback(self) -> None:
        # Remove pickled files
        for file_path in self.world_path.iterdir():
            if not file_path.is_file():
                continue
            if file_path.suffix == ".pkl":
                os.remove(file_path)
        
        # Move backup files to pickled files
        for file_path in self.world_path.iterdir():
            if not file_path.is_file():
                continue
            if file_path.suffix == ".backup":
                shutil.move(
                    src=file_path,
                    dst=file_path.with_suffix(".pkl")
                )
