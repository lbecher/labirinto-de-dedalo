import pygame

from game_mode import *
from player import *
from maze import *

# modo de jogo
use_ai = set_game_mode()

# configurações do pygame
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True
dt = 0

# configurações do labirinto
maze_matrix = load_maze_matrix()
maze_rows, maze_columns = get_maze_matrix_dimensions(maze_matrix)

while running:
    # captura eventos
    for event in pygame.event.get():
        # pygame.QUIT significa que a janela foi fechada
        if event.type == pygame.QUIT:
            running = False

    # preenche a tela com a cor preta, para limpar o frame anterior
    screen.fill("black")

    # dezenha o labirinto
    draw_maze(screen, maze_matrix, maze_rows, maze_columns)

    # draw sprites
    sprites = pygame.sprite.Group()
    sprites.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
