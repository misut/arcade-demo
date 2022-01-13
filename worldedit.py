from paradox.windows.settings import WorldEditSettings
from paradox.windows.worldedit import WorldEditWindow


if __name__ == "__main__":
    window = WorldEditWindow(WorldEditSettings())
    window.run()
