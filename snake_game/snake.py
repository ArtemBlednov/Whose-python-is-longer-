import pygame

class Snake:
    def __init__(self, mode=1):
        self.snake1 = [[5, 5]]  # Начальная позиция в квадратах
        self.dir1 = [1, 0]  # Вектор направления
        self.next_dir1 = self.dir1  # Промежуточный вектор направления для безопасной проверки
        self.score1 = 0  # Счет игрока / игрока 1

        self.snake2 = [[15, 15]] if mode == 2 else None  # Начальная позиция в квадратах
        self.dir2 = [-1, 0]  # Вектор направления
        self.next_dir2 = self.dir2  # Промежуточный вектор направления для безопасной проверки
        self.score2 = 0  # Счет игрока 2

        self.mode = mode

    def handle_input(self, keys):
        # Игрок 1 управление (WASD)
        if keys[pygame.K_w] and self.dir1 != [0, 1]:
            self.next_dir1 = [0, -1]
        elif keys[pygame.K_s] and self.dir1 != [0, -1]:
            self.next_dir1 = [0, 1]
        elif keys[pygame.K_a] and self.dir1 != [1, 0]:
            self.next_dir1 = [-1, 0]
        elif keys[pygame.K_d] and self.dir1 != [-1, 0]:
            self.next_dir1 = [1, 0]

        # Игрок 2 управление (стрелки)
        if self.mode == 2:
            if keys[pygame.K_UP] and self.dir2 != [0, 1]:
                self.next_dir2 = [0, -1]
            elif keys[pygame.K_DOWN] and self.dir2 != [0, -1]:
                self.next_dir2 = [0, 1]
            elif keys[pygame.K_LEFT] and self.dir2 != [1, 0]:
                self.next_dir2 = [-1, 0]
            elif keys[pygame.K_RIGHT] and self.dir2 != [-1, 0]:
                self.next_dir2 = [1, 0]

    def update(self, apple, spawn_apple, cfg):
        self.dir1 = self.next_dir1
        new_head1 = [self.snake1[0][0] + self.dir1[0], self.snake1[0][1] + self.dir1[1]]

        if (new_head1 in self.snake1 or
                (self.mode == 2 and new_head1 in self.snake2) or
                new_head1[0] < 0 or new_head1[0] >= cfg.GRID_WIDTH or
                new_head1[1] < 0 or new_head1[1] >= cfg.GRID_HEIGHT):
            return True, "2" if self.mode == 2 else None, apple

        self.snake1.insert(0, new_head1)
        if new_head1 == apple:
            self.score1 += 1
            apple = spawn_apple(self.snake1, self.snake2)
        else:
            self.snake1.pop()

        if self.mode == 2:
            self.dir2 = self.next_dir2
            new_head2 = [self.snake2[0][0] + self.dir2[0], self.snake2[0][1] + self.dir2[1]]

            if (new_head2 in self.snake2 or new_head2 in self.snake1 or
                    new_head2[0] < 0 or new_head2[0] >= cfg.GRID_WIDTH or
                    new_head2[1] < 0 or new_head2[1] >= cfg.GRID_HEIGHT):
                return True, "1", apple

            self.snake2.insert(0, new_head2)
            if new_head2 == apple:
                self.score2 += 1
                apple = spawn_apple(self.snake1, self.snake2)
            else:
                self.snake2.pop()

        return False, None, apple