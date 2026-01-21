class Solid:
    def __init__(self, position_x: int, position_y: int, radius: int | None) -> None:
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius

    def cercle(self):
        super().__init__(self,800,800,50)
        self.radius = 5


    def rectangle(self):
        pass