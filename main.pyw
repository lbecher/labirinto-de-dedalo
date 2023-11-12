import pygame

from player import *
from maze import load_maze_matrix, draw_maze

# maze setup
maze_matrix = load_maze_matrix()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1024, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos_2 = pygame.Vector2(screen.get_width() / 2 + 50, screen.get_height() / 2)

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

    pygame.draw.circle(screen, "red", player_pos, 40)
    pygame.draw.circle(screen, "blue", player_pos_2, 40)

    player_moviment(pygame, dt, player_pos)
    player_moviment(pygame, dt, player_pos_2)

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
