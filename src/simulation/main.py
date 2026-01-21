import arcade
from modules.human import Human
from random import randint

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
                             10, 5, 50) for _ in range(50)]

        for human in self.humans:
            self.sprites.append(human)

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
