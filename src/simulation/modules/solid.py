import numpy as np

class Obstacle:
    def __init__(self, position, radius=1.0):
        self.position = np.array(position, dtype=float)
        self.radius = radius

    def contains(self, point):
        """
        Test si un point est à l'intérieur de l'obstacle
        """
        return np.linalg.norm(point - self.position) < self.radius


def cercle(self):
     pass

def rectangle(self):
    pass