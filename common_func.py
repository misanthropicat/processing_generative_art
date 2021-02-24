from typing import Tuple

import numpy as np
import random
from datetime import datetime


def get_points_coordinates(x_interval: Tuple[float, float], y_interval: Tuple[float, float], num_points: int):
    x_bounds = np.array(x_interval)
    y_bounds = np.array(y_interval)
    x = np.random.uniform(*x_bounds, size=num_points).reshape(num_points, 1)
    y = np.random.uniform(*y_bounds, size=num_points).reshape(num_points, 1)
    pts = np.hstack([x, y])
    return pts


random.seed(datetime.now())


def get_color():
    return dict(r=random.randint(0, 255),
                g=random.randint(0, 255),
                b=random.randint(0, 255))


def get_mono():
    return dict(gray=random.randint(0, 255),
                alpha=random.randint(0, 255))


def draw_recursively_3(func, x1, y1, z1, x2, y2, z2):
    func(x1, y1, z1, x2, y2, z2)
    x1 /= 2
    y1 /= 2
    z1 /= 2
    x2 /= 2
    y2 /= 2
    z2 /= 2
    if x1 < 1 or y1 < 1 or z1 < 1:
        return
    draw_recursively_3(func, x1, y1, z1, x2, y2, z2)