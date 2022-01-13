from enum import Enum, unique


@unique
class Language(str, Enum):
    ENGLISH: str = "english"
    KOREAN: str = "korean"
