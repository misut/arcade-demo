from abc import ABC, abstractmethod
from typing import BinaryIO, Dict, Optional
import pickle

from paradox.domain.models import World



class AbstracWorldRepository(ABC):
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


class FileWorldRepository(AbstracWorldRepository):
    stream: BinaryIO
    mapping: Dict[str, World]

    def __init__(self, stream: BinaryIO) -> None:
        self.stream = stream
        try:
            self.mapping = pickle.load(self.stream)
        except EOFError:
            self.mapping = {}

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
