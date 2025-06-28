import pygame
import config as cfg
from .render import Render

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.render = Render(self.screen)

    def show_menu(self):
        self.screen.fill(cfg.BG_COLOR)

        self.render.draw_text("Змейка", 60, -100)
        self.render.draw_text("1. Одиночная игра (нажми 1)", 36, -20)
        self.render.draw_text("2. Два игрока (нажми 2)", 36, 30)

    def handle_menu(self):
        keys = pygame.key.get_pressed()     # Массив с состоянием кнопок (True / False)
        if keys[pygame.K_1]:
            return 1
        elif keys[pygame.K_2]:
            return 2
