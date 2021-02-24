from p5 import *

from common_func import get_color

width, height = 1050, 700
y_coord = 0.0
iter = 0


def setup():
    size(width, height)
    background(255 - iter)
    get_style()


def get_style():
    color = get_color()
    color2 = get_color()
    stroke(**color2)
    fill(**color)


def draw():
    global y_coord, iter
    for i in range(0, int(width / 50)):
        square((100 * i + 25, y_coord), 50, mode='CENTER')
    y_coord += 10
    if y_coord > height:
        y_coord = 0
        background(255 - iter * 20)
        iter += 1
        get_style()


if __name__ == '__main__':
    run()