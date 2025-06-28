import pygame
import config as cfg
from snake_game.apple import Apple

class Render:
    def __init__(self, screen):
        self.screen = screen

    def update_screen(self):
        pygame.display.flip()

    # Отрисовка сетки игрового поля
    def draw_grid(self):
        self.screen.fill(cfg.BG_COLOR)
        # Вертикальные линии
        for x in range(0, cfg.WINDOW_SIZE, cfg.CELL_SIZE):
            pygame.draw.line(self.screen, cfg.GRID_COLOR, (x, 0), (x, cfg.WINDOW_SIZE))
        # Горизонтальные линии
        for y in range(0, cfg.WINDOW_SIZE, cfg.CELL_SIZE):
            pygame.draw.line(self.screen, cfg.GRID_COLOR, (0, y), (cfg.WINDOW_SIZE, y))

    # Рендеринг текста на экране
    def draw_text(self, text, size=36, y_offset=0, center=True, color=cfg.WHITE):  # y_offset - вертикальное смещение
        f = pygame.font.SysFont(None, size)
        rendered = f.render(text, True, color)
        rect = rendered.get_rect()
        if center:
            rect.center = (cfg.WINDOW_SIZE // 2, cfg.WINDOW_SIZE // 2 + y_offset)
        else:
            rect.topleft = (10, 10 + y_offset)
        self.screen.blit(rendered, rect)

    # Рендеринг яблока
    def draw_apple(self, pos):
        pygame.draw.rect(self.screen,
                         cfg.RED,
                    (pos[0] * cfg.CELL_SIZE, pos[1] * cfg.CELL_SIZE, cfg.CELL_SIZE, cfg.CELL_SIZE)
                         )

    # Рендеринг змеи
    def draw_snake(self, snake, color_head, color_body):
        for i, seg in enumerate(snake):
            color = color_head if i == 0 else color_body
            pygame.draw.rect(self.screen,
                             color,
                             (seg[0] * cfg.CELL_SIZE, seg[1] * cfg.CELL_SIZE, cfg.CELL_SIZE, cfg.CELL_SIZE)
                             )








