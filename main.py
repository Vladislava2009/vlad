import pygame
import pygame
import sys

# Инициализация Pygame
pygame.init()

# Параметры окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Rectangle")

# Параметры прямоугольника
rect_width = 60
rect_height = 40
rect_x = screen_width // 2 - rect_width // 2
rect_y = screen_height // 2 - rect_height // 2
rect_color = (250, 0, 100)
move_distance = 200
move_speed = 2

# Параметры движения
is_moving = False
initial_x = rect_x
move_direction = 1  # 1: вправо, -1: влево

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_moving:
                is_moving = True

    if is_moving:
        rect_x += move_speed * move_direction
        if rect_x >= initial_x + move_distance:
            move_direction = -1  # Меняем направление на влево
        elif rect_x <= initial_x - move_distance:
            move_direction = 1  # Меняем направление на вправо

    # Отрисовка
    screen.fill((100, 250, 100))  # Очистка экрана черным цветом
    pygame.draw.rect(screen, rect_color, (rect_x, rect_y, rect_width, rect_height))
    pygame.display.flip()  # Обновление экрана
pygame.quit()
sys.exit()
import pygame
import sys
