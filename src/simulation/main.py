import arcade

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        pass

    def update(self, delta_time):
        pass

def main():
    pass

if __name__ == "__main__":
    main()