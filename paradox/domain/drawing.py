from typing import List, Sequence,Tuple, Union

import arcade

_Color = Union[List[int], Tuple[int, int, int], Tuple[int, int, int, int]]

SQRT_THREE = 3 ** (1 / 2)


def get_cube_points(
    center_x: float,
    center_y: float,
    side: float,
) -> Sequence[Union[Tuple[float, float], List[float]]]:
    side_half = side / 2
    side_half_sqrt_three = side_half * SQRT_THREE
    return [
        (center_x, center_y + side),
        (center_x + side_half_sqrt_three, center_y + side_half),
        (center_x + side_half_sqrt_three, center_y - side_half),
        (center_x, center_y - side),
        (center_x - side_half_sqrt_three, center_y - side_half),
        (center_x - side_half_sqrt_three, center_y + side_half),
    ]


def create_cube(
    center_x: float,
    center_y: float,
    side: float,
    color_list: List[_Color]
) -> arcade.ShapeElementList:
    center = (center_x, center_y)
    points = get_cube_points(center_x, center_y, side)
    cube = arcade.ShapeElementList()

    left = arcade.create_polygon(
        [center, points[1], points[2], points[3]],
        color_list[0]
    )
    cube.append(left)

    right = arcade.create_polygon(
        [center, points[3], points[4], points[5]],
        color_list[1]
    )
    cube.append(right)

    top = arcade.create_polygon(
        [center, points[5], points[0], points[1]],
        color_list[2]
    )
    cube.append(top)

    return cube
