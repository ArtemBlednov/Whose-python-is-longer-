import pygame
import sys
import config as cfg
from .render import Render

class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.render = Render(self.screen)

    def show_menu(self, winner=None):
        self.screen.fill(cfg.BG_COLOR)

        if winner:
            self.render.draw_text(f"Победил Игрок {winner}!", 48, -50)
            self.render.draw_text("Нажми R — сыграть снова", 36, 20)
            self.render.draw_text("Нажми M — вернуться в меню", 36, 60)
        else:
            self.render.draw_text("Ты проиграл!", 48, -50)
            self.render.draw_text("Нажми R — сыграть снова", 36, 20)
            self.render.draw_text("Нажми M — вернуться в меню", 36, 60)

        pygame.display.flip()

    def handle_menu(self, winner=None):
        while True:
            self.show_menu(winner)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return "running"
            elif keys[pygame.K_m]:
                return "main_menu"