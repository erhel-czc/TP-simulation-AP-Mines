import numpy as np

class Obstacle:
    def __init__(self, position_x, position_y, radius=1.0):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def contains(self, point):
        return np.linalg.norm(point - self.position) < self.radius
