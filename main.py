import pygame
import config as cfg



pygame.init()
screen = pygame.display.set_mode((cfg.WINDOW_SIZE, cfg.WINDOW_SIZE))
pygame.display.set_caption(cfg.WINDOW_CAPTION)
clock = pygame.time.Clock()

