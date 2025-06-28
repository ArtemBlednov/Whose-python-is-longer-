import random
import config as cfg

class Apple:
    def __init__(self, snake1, snake2=None):
        self.snake1 = snake1
        self.snake2 = snake2
        self.pos = self.spawn()

    def spawn(self):
        while True:
            pos = [random.randint(0, cfg.GRID_WIDTH - 1), random.randint(0, cfg.GRID_HEIGHT - 1)]
            if pos not in self.snake1 and (self.snake2 is None or pos not in self.snake2):
                return pos
