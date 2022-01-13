from arcade import View, Window

from paradox.windows.worldedit.views.intro import IntroView


intro: View = None

def init_views(window: Window) -> None:
    global intro

    intro = IntroView(window=window)
