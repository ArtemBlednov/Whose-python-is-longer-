import pygame
import random
import config as cfg
from snake_game.apple import Apple
from snake_game.ui.render import Render
from snake_game.ui.main_menu import MainMenu
from snake_game.ui.game_over_menu import GameOver
from snake_game.snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((cfg.WINDOW_SIZE, cfg.WINDOW_SIZE))
        pygame.display.set_caption('Whose python is longer')

        self.clock = pygame.time.Clock()
        self.running = True

        self.main_menu = MainMenu(self.screen)
        self.game_over = GameOver(self.screen)
        self.render = Render(self.screen)




    def run(self):
        state = 'main_menu'
        mode = None

        while self.running:
            self.clock.tick(cfg.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if state == 'main_menu':
                self.main_menu.show_menu()
                mode = self.main_menu.handle_menu()

                if mode is not None:
                    snake = Snake(mode=mode)
                    apple = spawn_apple(snake.snake1, snake.snake2)
                    state = 'running'

            elif state == 'running':
                if snake is None:
                    snake = Snake(mode=mode)
                    apple = spawn_apple(snake.snake1, snake.snake2)


                keys = pygame.key.get_pressed()
                snake.handle_input(keys)
                game_over, winner, apple = snake.update(apple, spawn_apple, cfg)

                self.render.draw_grid()

                if snake.mode == 1:
                    self.render.draw_snake(snake.snake1, cfg.GREEN, cfg.DARK_GREEN)
                    self.render.draw_text(f"Счёт: {snake.score1}", 28, 0, center=False)

                elif snake.mode == 2:
                    self.render.draw_snake(snake.snake1, cfg.BLUE, cfg.DARK_BLUE)
                    self.render.draw_snake(snake.snake2, cfg.YELLOW, cfg.DARK_YELLOW)
                    self.render.draw_text(f"Игрок 1: {snake.score1}", 28, 0, center=False)
                    self.render.draw_text(f"Игрок 2: {snake.score2}", 28, 30, center=False)

                self.render.draw_apple(apple)

                if game_over:
                    state = 'game_over'

            elif state == 'game_over':
                action = self.game_over.handle_menu(winner)

                if action == 'running':
                    snake = None
                    state = 'running'
                elif action == 'main_menu':
                    state = 'main_menu'

            self.render.update_screen()


def spawn_apple(snake1, snake2=None):
    return Apple(snake1, snake2).pos



