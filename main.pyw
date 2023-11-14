import pygame

from player import *
from maze import *


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
running = True
dt = 0

# maze setup
maze_matrix = load_maze_matrix()

# players setup
player1_position = find_player1(pygame, maze_matrix)
player2_position = find_player2(pygame, maze_matrix)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # maze
    draw_maze(pygame, screen, maze_matrix)

    # player spawnpos
    pygame.draw.circle(screen, "red", player1_position, 32)
    pygame.draw.circle(screen, "blue", player2_position, 32)

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
