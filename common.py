import pygame

from constants import *

def maze_to_pygame_coordinates(i, j):
    final_tile_length = TILE_LENGTH * TILE_SCALE
    tile_center = final_tile_length / 2
    x_len = (j * final_tile_length)
    y_len = (i * final_tile_length)
    x_coord, y_coord = x_len + tile_center, y_len + tile_center
    return pygame.Vector2(x_coord, y_coord)
