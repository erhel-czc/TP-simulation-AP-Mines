import arcade
from modules.human import Human
from random import randint
from modules.solid import Solid 


class Window(arcade.Window):
    ## créer deux humains et les afficher
    def __init__(self, width: int = 800, height: int = 600, title: str = "Simulation"):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.setup()

    def setup(self):
        self.sprites = arcade.SpriteList()

        self.humans = [Human(randint(0, self.width),
                             randint(0, self.height),
                             10, 2, 50,
                             self.width, self.height) for _ in range(100)]

        for human in self.humans:
            self.sprites.append(human)

        self.start = Solid(randint(50, self.width - 50), randint(50, self.height - 50))

        while True:
            self.end = Solid(randint(50, self.width - 50), randint(50, self.height - 50))
            if not self.end.collides_with(self.start):
                break


        self.sprites.append(self.start)
        self.sprites.append(self.end)

    def on_draw(self):
        self.clear()
        self.sprites.draw()
        pass

    def on_update(self, delta_time):
        for human in self.humans:
            human.move()
        self.sprites.update()

def main():
    pass

if __name__ == "__main__":
    window = Window()
    arcade.run()
