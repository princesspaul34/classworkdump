from tkinter import font

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Snake Dash 1")
font = pygame.font.Font(None, 36)
cell_size = 30
number_of_cells = 20
def start_game():
    return [(9, 10), (8, 10), (7, 10)], (12, 10), 1, 0, 0, False
snake_body, food_position, direction_x, direction_y, score, game_over = start_game()


MOVE_SNAKE = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_SNAKE, 200)

game_running = True

while game_running:

    # Check events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            game_running = False

        # Change direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction_y != 1:
                direction_x, direction_y = 0, -1

            elif event.key == pygame.K_DOWN and direction_y != -1:
                direction_x, direction_y = 0, 1

            elif event.key == pygame.K_LEFT and direction_x != 1:
                direction_x, direction_y = -1, 0

            elif event.key == pygame.K_RIGHT and direction_x != -1:
                direction_x, direction_y = 1, 0

        # Move snake
        if event.type == MOVE_SNAKE and not game_over:
            head_x, head_y = snake_body[0]; snake_body.insert(0, (head_x + direction_x, head_y + direction_y))
            head_x, head_y = snake_body[0]
            #outside_board = head_x < 0 or head_x >= number_of_cells or head_y < 0 or head_y >= number_of_cells
            #touched_tail = snake_body[0] in snake_body[1:]
            #if outside_board or touched_tail:
                #game_over = True
            if head_x < 0 or head_x >= 20 or head_y < 0 or head_y >= 20 or snake_body[0] in snake_body[1:]: game_over = True
            elif snake_body[0] == food_position:
               score += 1
               food_position = (random.randint(0, 19), random.randint(0, 19))
            else: snake_body.pop()
    # Draw background
    screen.fill((173, 204, 96) if game_over else (173, 204, 96))
    if not game_over: pygame.draw.rect(screen, (220, 70, 70), (food_position[0] * cell_size, food_position[1] * cell_size, cell_size, cell_size))
    for body_square in snake_body: pygame.draw.rect(screen, (43, 51, 24), (body_square[0] * cell_size, body_square[1] * cell_size, cell_size, cell_size))
    message = "score: " + str(score) if not game_over else "Game Over! press SPACE"
    screen.blit(font.render(message, True, (43, 51, 24)), (15, 610))
    pygame.display.update()

pygame.quit()
