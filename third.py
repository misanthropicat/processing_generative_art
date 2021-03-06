from p5 import *

from common_func import get_mono, get_contrasted

width, height = 1024, 768
total_degrees = 360


def setup():
    size(width, height)
    monochrome = get_mono()
    background(monochrome['gray'])
    contrasted = get_contrasted(monochrome)
    stroke(**contrasted)
    no_loop()
    no_fill()


def draw():
    side_length = 50
    begin_contour()
    for i in range(total_degrees):
        x = width - side_length * cos(radians(i))
        y = height - side_length * sin(radians(i))
        curve_vertex(x, y)
    end_contour()


if __name__ == '__main__':
    run(frame_rate=25)