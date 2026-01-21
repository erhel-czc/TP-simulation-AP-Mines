import arcade
from math import exp

def sign(x: float) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

class Human(arcade.SpriteCircle):
    """store alle humans created in a list called humans"""
    humans: list["Human"] = []

    def __init__(self, init_x: int, init_y: int, size: int, max_speed: int, d_0: int) -> None:
        super().__init__(size, arcade.color.BLUE)
        self.center_x = init_x
        self.center_y = init_y
        self.max_speed = max_speed
        self.d_0 = d_0
        
        Human.humans.append(self)

    def move(self) -> None:
        delta_x, delta_y = self.compute_deltas()
        self.center_x += delta_x + self.max_speed
        self.center_y += delta_y

    def compute_deltas(self) -> tuple[float, float]:
        other_humans = [human for human in Human.humans if human != self]

        delta_x = 0.0
        delta_y = 0.0

        for other in other_humans:
            d_x = other.center_x - self.center_x
            d_y = other.center_y - self.center_y

            delta_x += -sign(d_x)*self.max_speed*exp(-abs(d_x)/self.d_0)
            delta_y += -sign(d_y)*self.max_speed*exp(-abs(d_y)/self.d_0)

        return delta_x, delta_y