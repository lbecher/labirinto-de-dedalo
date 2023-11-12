from constants import *
from sprite import Sprite

def load_maze_matrix():
    matrix = []
    with open("maze.txt", 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
    return matrix

def get_matrix_dimensions(matrix):
    rows = len(matrix)
    columns = len(matrix[0]) if matrix else 0
    return rows, columns

def draw_maze(pygame, screen, maze_matrix):
    rows, columns = get_matrix_dimensions(maze_matrix)
    final_tile_length = TILE_SCALE * TILE_LENGTH
    tile_center = (final_tile_length) / 2
    for i in range(0, rows):
        y_len = (i * final_tile_length)
        for j in range(0, columns):
            x_len = (j * final_tile_length)
            x_pos, y_pos = x_len + tile_center, y_len + tile_center
            pos = pygame.Vector2(x_pos, y_pos)
            if maze_matrix[i][j] == 0:
                pygame.draw.circle(screen, "gray", pos, final_tile_length / 2)
            elif maze_matrix[i][j] == 1:
                pygame.draw.circle(screen, "green", pos, final_tile_length / 2)
            elif maze_matrix[i][j] == 2:
                pygame.draw.circle(screen, "orange", pos, final_tile_length / 2)
            elif maze_matrix[i][j] == 3:
                pygame.draw.circle(screen, "purple", pos, final_tile_length / 2)
