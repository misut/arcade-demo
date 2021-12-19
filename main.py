import arcade

from paradox.drawing import create_cube, create_cube_with_border

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Shape List Demo 3"

HALF_SQUARE_WIDTH = 2.5
HALF_SQUARE_HEIGHT = 2.5
SQUARE_SPACING = 10


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.DARK_SLATE_GRAY)

        self.draw_time = 0
        self.shape_list = None

    def setup(self):
        self.shape_list = create_cube_with_border(
            center_x=100,
            center_y=100,
            side=100,
            color_list=[
                arcade.color.RED,
                arcade.color.GREEN,
                arcade.color.BLUE,
            ],
            line_width=3.0
        )

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # --- Draw all the rectangles
        self.shape_list.draw()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()