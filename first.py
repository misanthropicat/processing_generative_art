from p5 import *

from common_func import get_mono, get_color, draw_recursively_3

width, height = 1024, 768


def setup():
    size(width, height)
    monochrome = get_mono()
    background(**monochrome)
    get_style()


def get_style():
    color = get_color()
    monochrome = get_mono()
    stroke(**color)
    fill(**monochrome)


def draw_recursively_2(func, x, y, h, w, x_step, y_step, h_step, w_step):
    func(x, y, h, w)
    x += x_step
    y += y_step
    h *= h_step
    w *= w_step
    if x >= width or y >= height or h >= height or w >= width:
        return
    draw_recursively_2(func, x, y, h, w, x_step, y_step, h_step, w_step)


def draw():
    monochrome = get_mono()
    background(**monochrome)
    x, y, z = width / 2, height / 2, 0
    h, w = 50, 50
    x_step, y_step = 1, 1
    h_step, w_step = 1.05, 1.05
    get_style()
    draw_recursively_2(ellipse, x, y, h, w, x_step, y_step, h_step, w_step)
    color = get_color()
    background(**color)
    x, y = 0, height / 2
    h, w = 10, 50
    x_step, y_step = 10, 1
    h_step, w_step = 1.03, 1.01
    draw_recursively_2(rect, x, y, h, w, x_step, y_step, h_step, w_step)
    monochrome = get_mono()
    background(**monochrome)
    color = get_color()
    background(**color)
    x1, y1, z1 = width, height, 50
    x2, y2, z2 = width / 2, height / 2, 25
    draw_recursively_3(triangle, x1, y1, z1, x2, y2, z2)


def mouse_pressed():
    get_style()
    stroke_weight(2)
    monochrome = get_mono()
    y = 1
    while y < height:
        background(**monochrome)
        line(0, y, width, y)
        y *= 1.025


if __name__ == '__main__':
    run(frame_rate=15)