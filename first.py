import random
from datetime import datetime
from typing import Tuple

from p5 import *

random.seed(datetime.now())
width, height = 1024, 768


def get_color():
    return dict(r=random.randint(0, 255),
                g=random.randint(0, 255),
                b=random.randint(0, 255))


def get_mono():
    return dict(gray=random.randint(0, 255),
                alpha=random.randint(0, 255))


def setup():
    size(width, height)
    monochrome = get_mono()
    background(**monochrome)
    get_style()


def get_style():
    color = get_color()
    monochrome = get_mono()
    no_stroke()
    stroke(**color)
    fill(**monochrome)


def get_position(start: Tuple[int, int], x_step: int, y_step: int):
    st_width, st_height = start
    return st_width + x_step, st_height + y_step


def draw_recursively(func, x, y, h, w, x_step, y_step, h_step, w_step):
    func(x, y, h, w)
    x += x_step
    y += y_step
    h *= h_step
    w *= w_step
    if x == width or y == height:
        return
    draw_recursively(func, x, y, h, w, x_step, y_step, h_step, w_step)


def draw():
    x, y = width / 2, height / 2
    h, w = 100, 100
    x_step, y_step = 1, 1
    h_step, w_step = 1.01, 1.01
    draw_recursively(ellipse, x, y, h, w, x_step, y_step, h_step, w_step)


def mouse_pressed():
    redraw()


if __name__=='__main__':
    run(frame_rate=15)