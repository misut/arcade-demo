from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, BinaryIO
import os
import pickle
import shutil

from paradox.infrastructure.repository import (
    AbstracWorldRepository,
    FileWorldRepository,
)


class AbstractWorldUnitOfWork(ABC):
    worlds: AbstracWorldRepository

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
    file_path: str
    stream: BinaryIO

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path
    
    def __enter__(self) -> FileWorldUnitOfWork:
        self.stream = open(self.file_path, "rb+")
        self.worlds = FileWorldRepository(self.stream)
        shutil.copyfile(
            src=self.file_path,
            dst=self.file_path+".backup"
        )
        return super().__enter__()

    def __exit__(self, *args: Any) -> None:
        self.stream.close()
        os.remove(self.file_path+".backup")
        super().__exit__(*args)

    def commit(self) -> None:
        pickle.dump(self.worlds.mapping, self.stream)

    def rollback(self) -> None:
        shutil.copyfile(
            src=self.file_path+".backup",
            dst=self.file_path
        )
