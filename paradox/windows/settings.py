from pathlib import Path
import pydantic


class WorldEditSettings(pydantic.BaseSettings):
    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int
    WINDOW_SCALE: float
    FULLSCREEN: bool

    TEXTS_PATH: Path
    WORLDS_PATH: Path

    class Config:
        env_file = ".env"
        env_prefix = "PARADOX_"
