import numpy as np
import matplotlib.pyplot as plt

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.random.choice([0, 1], size=(height, width))

    def update(self):
        new_grid = self.grid.copy()
        for y in range(self.height):
            for x in range(self.width):
                # Count live neighbors
                total = (self.grid[y, (x-1)%self.width] + self.grid[y, (x+1)%self.width] +
                         self.grid[(y-1)%self.height, x] + self.grid[(y+1)%self.height, x] +
                         self.grid[(y-1)%self.height, (x-1)%self.width] + self.grid[(y-1)%self.height, (x+1)%self.width] +
                         self.grid[(y+1)%self.height, (x-1)%self.width] + self.grid[(y+1)%self.height, (x+1)%self.width])

                # Apply rules
                if self.grid[y, x] == 1:
                    if total < 2 or total > 3:
                        new_grid[y, x] = 0  # Cell dies
                else:
                    if total == 3:
                        new_grid[y, x] = 1  # Cell becomes alive

        self.grid = new_grid

    def display(self):
        plt.imshow(self.grid, cmap='binary')
        plt.axis('off')
        plt.show()

if __name__ == '__main__':
    game = GameOfLife(width=100, height=100)
    for _ in range(100):
        game.display()
        game.update()