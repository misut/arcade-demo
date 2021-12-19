import pydantic


class WorldEditSettings(pydantic.BaseSettings):
    WINDOW_WIDTH: int
    WINDOW_HEIGHT: int

    class Config:
        env_file = ".env"
        env_prefix = "PARADOX_"
