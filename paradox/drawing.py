from typing import List, Tuple, Union

import arcade

_Color = Union[List[int], Tuple[int, int, int], Tuple[int, int, int, int]]

SQRT_THREE = 3 ** (1 / 2)


def create_cube(
    center_x: float,
    center_y: float,
    side: float,
    color_list: List[_Color]
) -> arcade.ShapeElementList:
    cube = arcade.ShapeElementList()
    side_half = side / 2
    side_half_sqrt_three = side_half * SQRT_THREE

    point_dict = {
        "clock_0": [center_x, center_y + side],
        "clock_2": [center_x + side_half_sqrt_three, center_y + side_half],
        "clock_4": [center_x + side_half_sqrt_three, center_y - side_half],
        "clock_6": [center_x, center_y - side],
        "clock_8": [center_x - side_half_sqrt_three, center_y - side_half],
        "clock_10": [center_x - side_half_sqrt_three, center_y + side_half],
        "center": [center_x, center_y],
    }

    left = arcade.create_polygon(
        [point_dict["center"], point_dict["clock_6"], point_dict["clock_8"], point_dict["clock_10"]],
        color_list[1]
    )
    cube.append(left)

    right = arcade.create_polygon(
        [point_dict["center"], point_dict["clock_2"], point_dict["clock_4"], point_dict["clock_6"]],
        color_list[2]
    )
    cube.append(right)

    top = arcade.create_polygon(
        [point_dict["clock_0"], point_dict["clock_2"], point_dict["center"], point_dict["clock_10"]],
        color_list[0]
    )
    cube.append(top)

    return cube


def create_cube_with_border(
    center_x: float,
    center_y: float,
    side: float,
    color_list: List[_Color],
    line_width: float
) -> arcade.ShapeElementList:
    cube = arcade.ShapeElementList()
    side_half = side / 2
    side_half_sqrt_three = side_half * SQRT_THREE

    point_dict = {
        "clock_0": [center_x, center_y + side],
        "clock_2": [center_x + side_half_sqrt_three, center_y + side_half],
        "clock_4": [center_x + side_half_sqrt_three, center_y - side_half],
        "clock_6": [center_x, center_y - side],
        "clock_8": [center_x - side_half_sqrt_three, center_y - side_half],
        "clock_10": [center_x - side_half_sqrt_three, center_y + side_half],
        "center": [center_x, center_y],
    }

    point_list = [point_dict["center"], point_dict["clock_6"], point_dict["clock_8"], point_dict["clock_10"]]
    left = arcade.create_polygon(point_list, color_list[1])
    cube.append(left)

    left_border = arcade.create_line_loop(point_list, arcade.color.DARK_CYAN, line_width)
    cube.append(left_border)

    point_list = [point_dict["center"], point_dict["clock_2"], point_dict["clock_4"], point_dict["clock_6"]]
    right = arcade.create_polygon(point_list, color_list[2])
    cube.append(right)

    right_border = arcade.create_line_loop(point_list, arcade.color.DARK_BLUE, line_width)
    cube.append(right_border)

    point_list = [point_dict["clock_0"], point_dict["clock_2"], point_dict["center"], point_dict["clock_10"]]
    top = arcade.create_polygon(point_list, color_list[0])
    cube.append(top)

    top_border = arcade.create_line_loop(point_list, arcade.color.DARK_RED, line_width)
    cube.append(top_border)

    return cube
