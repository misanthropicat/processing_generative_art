from p5 import *

from common_func import get_mono

width, height = 1050, 700
x = 0
y = 0
dim = 80.0
monochrome = get_mono()


def setup():
        size(width, height)
        no_stroke()


def draw():
        global x, monochrome
        x = x + 1.2
        background(**monochrome)
        if x > width + dim:
            x = -dim

        translate(x, round(height/2 - dim/2))
        fill(255)
        rect((-dim/2, -dim/2), dim, dim)

        # Transforms accumulate. Notice how this rect moves
        # twice as fast as the other, but it has the same
        # parameter for the x-axis value
        translate(x, round(dim))
        fill(0)
        rect((-dim/2, -dim/2), dim, dim)


if __name__ == '__main__':
  run()