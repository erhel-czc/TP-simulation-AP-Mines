import numpy as np

class Obstacle:
    def __init__(self, position, radius=1.0):
        self.position_x = position
        self.radius = radius

    def contains(self, point):
        return np.linalg.norm(point - self.position) < self.radius
