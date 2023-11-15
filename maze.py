import pygame

from common import *
from constants import *

def load_maze_matrix():
    maze_matrix = []
    with open("maze.txt", 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            maze_matrix.append(row)
    return maze_matrix

def get_maze_matrix_dimensions(maze_matrix):
    maze_rows = len(maze_matrix)
    maze_columns = len(maze_matrix[0]) if maze_matrix else 0
    return maze_rows, maze_columns

def find_maze_end(maze_matrix, maze_rows, maze_columns):
    for i in range(0, maze_rows):
        for j in range(0, maze_columns):
            if maze_matrix[i][j] == MAZE_END:
                return i, j
    return None

def find_player1(maze_matrix, maze_rows, maze_columns):
    for i in range(0, maze_rows):
        for j in range(0, maze_columns):
            if maze_matrix[i][j] == PLAYER1:
                return i, j
    return None

def find_player2(maze_matrix, maze_rows, maze_columns):
    for i in range(0, maze_rows):
        for j in range(0, maze_columns):
            if maze_matrix[i][j] == PLAYER2:
                return i, j
    return None

def draw_maze(screen, maze_matrix, maze_rows, maze_columns):
    for i in range(0, maze_rows):
        for j in range(0, maze_columns):
            pygame_coordinates = maze_to_pygame_coordinates(i, j)
            pygame_position = pygame.Vector2(pygame_coordinates)
            if maze_matrix[i][j] == WALL:
                pygame.draw.circle(screen, "gray", pygame_position, 32)
            elif maze_matrix[i][j] == MAZE_END:
                pygame.draw.circle(screen, "purple", pygame_position, 32)
            else:
                pygame.draw.circle(screen, "green", pygame_position, 32)
