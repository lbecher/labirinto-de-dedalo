import pygame

from player import *
from maze import *

# configurações do pygame
pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# configurações do labirinto
maze_matrix = load_maze_matrix()
maze_rows, maze_columns = get_maze_matrix_dimensions(maze_matrix)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # maze
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
