import pygame

from constants import *
from maze import *

def is_valid_move(maze_matrix, i, j):
    if maze_matrix[i][j] == WALL:
        return False
    return True

def player1_keyboard_movement(maze_matrix, maze_rows, maze_columns, i, j):
    new_i = i
    new_j = j

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        new_i -= 1
    if keys[pygame.K_s]:
        new_i += 1
    
    if new_i < 0 or new_i >= maze_rows:
        new_i = i

    if keys[pygame.K_a]:
        new_j -= 1
    if keys[pygame.K_d]:
        new_j += 1
    
    if new_j < 0 or new_j >= maze_columns:
        new_j = j

    if not is_valid_move(maze_matrix, new_i, new_j):
        new_j = j
        new_i = i
    
    return new_i, new_j

def player2_keyboard_movement(maze_matrix, maze_rows, maze_columns, i, j):
    new_i = i
    new_j = j

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        new_i -= 1
    if keys[pygame.K_DOWN]:
        new_i += 1
    
    if new_i < 0 or new_i >= maze_rows:
        new_i = i

    if keys[pygame.K_LEFT]:
        new_j -= 1
    if keys[pygame.K_RIGHT]:
        new_j += 1
    
    if new_j < 0 or new_j >= maze_columns:
        new_j = j

    if not is_valid_move(maze_matrix, new_i, new_j):
        new_j = j
        new_i = i
    
    return new_i, new_j
