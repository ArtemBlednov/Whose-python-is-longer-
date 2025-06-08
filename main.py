import pygame
import sys
import random

# Настройки ############################################################################################################
WINDOW_SIZE = 600
CELL_SIZE = 20 # Размер квадрата (ВВОДИТЬ ТОЛЬКО КРАТНОЕ 10!!!)
GRID_WIDTH = WINDOW_SIZE // CELL_SIZE
GRID_HEIGHT = WINDOW_SIZE // CELL_SIZE
FPS = 13
########################################################################################################################

# Цвета ################################################################################################################
YELLOW = (255, 255, 0)
DARK_YELLOW = (200, 200, 0)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 150, 0)
BLUE = (0, 150, 255)
DARK_BLUE = (0, 100, 200)
RED = (200, 0, 0)
WHITE = (255, 255, 255)
BG_COLOR = (30, 30, 30)
GRID_COLOR = (50, 50, 50)
########################################################################################################################

# Инициализация PyGame и служебная часть ###############################################################################
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()
# font = pygame.font.SysFont(None, 36)
# big_font = pygame.font.SysFont(None, 60)
########################################################################################################################

# Сетка игрового поля ##################################################################################################
def draw_grid():
    # Вертикальные линии
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_SIZE))
    # Горизонтальные линии
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_SIZE, y))
########################################################################################################################

# Генерация яблока вне змейки ##########################################################################################
def spawn_apple(snake1, snake2=None):
    while True:
        pos = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
        if pos not in snake1 and (snake2 is None or pos not in snake2):
            return pos
########################################################################################################################

# Настройка текста на экране (настройки рендеринга) ####################################################################
def show_text(text, size=36, y_offset=0, center=True):  # y_offset - вертикальное смещение
    f = pygame.font.SysFont(None, size)
    rendered = f.render(text, True, WHITE)
    rect = rendered.get_rect()
    if center:
        rect.center = (WINDOW_SIZE // 2, WINDOW_SIZE // 2 + y_offset)
    else:
        rect.topleft = (10, 10 + y_offset)
    screen.blit(rendered, rect)
########################################################################################################################

# Главный экран (меню) #################################################################################################
def main_menu():
    while True:
        screen.fill(BG_COLOR)
        show_text("Змейка", 60, -100)
        show_text("1. Одиночная игра (нажми 1)", 36, -20)
        show_text("2. Два игрока (нажми 2)", 36, 30)
        pygame.display.flip() # Обновление (рендеринг) экрана

        for event in pygame.event.get():    # Завершение программы при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()       # Остановка модулей PyGame
                sys.exit()          # Полная остановка программы

        keys = pygame.key.get_pressed()     # Массив с состоянием кнопок (True / False)
        if keys[pygame.K_1]:
            game_loop(mode=1)       # Одиночная игра
        elif keys[pygame.K_2]:
            game_loop(mode=2)       # Режим игры с другом
########################################################################################################################

# Экран конца (GameOver) ###############################################################################################
def game_over_screen(winner=None):
    while True:
        screen.fill(BG_COLOR)
        if winner:
            show_text(f"Победил Игрок {winner}!", 48, -50)
        else:
            show_text("Ты проиграл!", 48, -50)
        show_text("Нажми R — сыграть снова", 36, 20)
        show_text("Нажми M — вернуться в меню", 36, 60)
        pygame.display.flip()

        for event in pygame.event.get():        # Завершение программы при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()       # Остановка модулей PyGame
                sys.exit()          # Полная остановка программы

        keys = pygame.key.get_pressed()         # Массив с состоянием кнопок (True / False)
        if keys[pygame.K_r]:
            return "restart"
        elif keys[pygame.K_m]:
            return "menu"
########################################################################################################################

# Основной игровой цикл (движок) #######################################################################################
def game_loop(mode=1):
    snake1 = [[5, 5]]   # Начальная позиция в квадратах
    dir1 = [1, 0]       # Вектор направления
    next_dir1 = dir1    # Промежуточный вектор направления для безопасной проверки
    score1 = 0          # Счет игрока / игрока 1

    snake2 = [[15, 15]] if mode == 2 else None  # Начальная позиция в квадратах
    dir2 = [-1, 0]      # Вектор направления
    next_dir2 = dir2    # Промежуточный вектор направления для безопасной проверки
    score2 = 0          # Счет игрока 2

    apple = spawn_apple(snake1, snake2)     # Генерация позиции яблок

    while True:
        clock.tick(FPS)     # Кадров в секунду

        for event in pygame.event.get():        # Завершение программы при нажатии на крестик
            if event.type == pygame.QUIT:
                pygame.quit()       # Остановка модулей PyGame
                sys.exit()

        keys = pygame.key.get_pressed()         # Массив с состоянием кнопок (True / False)

        # Игрок 1 управление (WASD)
        if keys[pygame.K_w] and dir1 != [0, 1]:
            next_dir1 = [0, -1]
        elif keys[pygame.K_s] and dir1 != [0, -1]:
            next_dir1 = [0, 1]
        elif keys[pygame.K_a] and dir1 != [1, 0]:
            next_dir1 = [-1, 0]
        elif keys[pygame.K_d] and dir1 != [-1, 0]:
            next_dir1 = [1, 0]

        # Игрок 2 управление (стрелки)
        if mode == 2:
            if keys[pygame.K_UP] and dir2 != [0, 1]:
                next_dir2 = [0, -1]
            elif keys[pygame.K_DOWN] and dir2 != [0, -1]:
                next_dir2 = [0, 1]
            elif keys[pygame.K_LEFT] and dir2 != [1, 0]:
                next_dir2 = [-1, 0]
            elif keys[pygame.K_RIGHT] and dir2 != [-1, 0]:
                next_dir2 = [1, 0]

        dir1 = next_dir1        # Обновление основного вектора направления
        new_head1 = [snake1[0][0] + dir1[0], snake1[0][1] + dir1[1]]    # Меняем положение головы по вектору направления

        # Проверка столкновений для 1
        if (new_head1 in snake1 or
            (mode == 2 and new_head1 in snake2) or
            new_head1[0] < 0 or new_head1[0] >= GRID_WIDTH or
            new_head1[1] < 0 or new_head1[1] >= GRID_HEIGHT):
            result = game_over_screen(winner="2" if mode == 2 else None)
            if result == "restart":
                game_loop(mode)
            else:
                main_menu()

        snake1.insert(0, new_head1) # Вставка новой головы в список сегментов змеи
        if new_head1 == apple:
            score1 += 1
            apple = spawn_apple(snake1, snake2)
        else:
            snake1.pop()                    # Удаление конца змеи (если голова не коснулась яблока)

        # Игрок 2
        if mode == 2:
            dir2 = next_dir2                # Обновление основного вектора направления
            new_head2 = [snake2[0][0] + dir2[0], snake2[0][1] + dir2[1]] # Меняем положение головы по вектору dir2

            # Проверка столкновений для 2
            if (new_head2 in snake2 or new_head2 in snake1 or
                new_head2[0] < 0 or new_head2[0] >= GRID_WIDTH or
                new_head2[1] < 0 or new_head2[1] >= GRID_HEIGHT):
                result = game_over_screen(winner="1")
                if result == "restart":
                    game_loop(mode)
                else:
                    main_menu()

            snake2.insert(0, new_head2)     # Вставка новой головы в список сегментов змеи
            if new_head2 == apple:
                score2 += 1
                apple = spawn_apple(snake1, snake2)
            else:
                snake2.pop()                        # Удаление конца змеи (если голова не коснулась яблока)

        # Рендеринг (отрисовка) ########################################################################################
        screen.fill(BG_COLOR)
        draw_grid()     # Сетка

        pygame.draw.rect(screen, RED, (apple[0]*CELL_SIZE, apple[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE)) # Яблоко

        # Отрисовка сегментов змеи 1
        for i, seg in enumerate(snake1):
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(screen, color, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if mode == 2:
            # Отрисовка сегментов змеи 2
            for i, seg in enumerate(snake2):
                color = BLUE if i == 0 else DARK_BLUE
                pygame.draw.rect(screen, color, (seg[0]*CELL_SIZE, seg[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Отрисовка сегментов змеи 1
            for i, seg in enumerate(snake1):
                color = YELLOW if i == 0 else DARK_YELLOW
                pygame.draw.rect(screen, color, (seg[0] * CELL_SIZE, seg[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Счет - бар
            show_text(f"Игрок 1: {score1}", 28, 0, center=False)
            show_text(f"Игрок 2: {score2}", 28, 30, center=False)
        else:
            show_text(f"Счёт: {score1}", 28, 0, center=False)

        pygame.display.flip()       # Обновление (рендеринг) экрана
        ################################################################################################################

# Запуск
main_menu()
