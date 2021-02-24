from p5 import *

from common_func import get_points_coordinates

width = 1920
height = 1080
iter = 0


def setup():
    size(width // 2, height // 2)
    background(iter)


def get_line_color():
    mono = dict(gray=255 - iter * 10)
    stroke(**mono)
    stroke_weight(2)


def draw_polygonal(corners: int, start_x: float, start_y: float, side_length: int):
    projection = side_length + 2 * sqrt(side_length**2 - (side_length/5)**2)
    x_coords = start_x, start_x - projection
    y_coords = start_y, start_y - projection
    points = get_points_coordinates(x_coords, y_coords, corners)
    begin_shape()
    [vertex(x, y) for x, y in points]
    end_shape(CLOSE)
    start_x = start_x / 2
    side_length = round(side_length * 0.8)
    if start_x < projection:
        return
    draw_polygonal(corners, start_x, start_y, side_length)
    start_y = start_y / 2
    if start_y < projection:
        return
    draw_polygonal(corners, start_x, start_y, side_length)


def draw():
    global iter
    get_line_color()
    side_length = 50
    draw_polygonal(8, width, height, side_length)
    if iter < 26:
        iter += 1
    else:
        iter -= 1


if __name__ == '__main__':
    run(frame_rate=25, mode="P2D")