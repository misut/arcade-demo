from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Optional
import json
import pickle

from pydantic import BaseModel, Field

from paradox.domain.enum import Language
from paradox.domain.models import World


class AbstractTextRepository(ABC, BaseModel):
    language: Language = Field(default=Language.ENGLISH)

    text_dict: Dict[str, str] = Field(default={})
    default_text_dict: Dict[str, str] = Field(default={})

    @abstractmethod
    def get(self, identifier: str) -> str:
        raise NotImplementedError


class FileTextRepository(AbstractTextRepository):
    text_path: Path
    
    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.setup()

    def _load_text_dict(self, language: Language = None) -> Dict[str, str]:
        if language is None:
            file_path = self.text_path.joinpath(f"{self.language}.json")
        else:
            file_path = self.text_path.joinpath(f"{language}.json")

        with file_path.open("rt", encoding="utf-8") as stream:
            text_dict = json.load(stream)

        return text_dict

    def setup(self) -> None:
        self.default_text_dict = self._load_text_dict(Language.ENGLISH)
        self.text_dict = self._load_text_dict()

    def get(self, identifier: str) -> str:
        text = self.text_dict.get(identifier, None)
        if text is None:
            text = self.default_text_dict.get(identifier, identifier)
        return text


class AbstractWorldRepository(ABC, BaseModel):
    mapping: Dict[str, World] = Field(default={})

    @abstractmethod
    def add(self, world: World) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def get(self, world_name: str) -> Optional[World]:
        raise NotImplementedError

    @abstractmethod
    def update(self, world: World) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def remove(self, world_name: str) -> Optional[World]:
        raise NotImplementedError


class FileWorldRepository(AbstractWorldRepository):
    world_path: Path

    def __init__(self, **data: Any) -> None:
        super().__init__(**data)
        self.setup()

    def setup(self) -> None:
        self.world_path.mkdir(parents=True, exist_ok=True)
        for file_path in self.world_path.iterdir():
            if not (file_path.is_file() and file_path.suffix == ".pkl"):
                continue

            with file_path.open("rb+") as stream:
                self.mapping[file_path.stem] = pickle.load(stream)
            

    def add(self, world: World) -> None:
        if world.name in self.mapping:
            raise Exception(f"World '{world.name}' already exists!")
        self.mapping[world.name] = world
    
    def get(self, world_name: str) -> Optional[World]:
        return self.mapping.get(world_name, None)
    
    def update(self, world: World) -> None:
        self.mapping[world.name] = world
    
    def remove(self, world_name: str) -> Optional[World]:
        return self.mapping.pop(world_name, None)
