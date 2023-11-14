from constants import *
from maze import *

def find_player1(pygame, maze_matrix):
    rows, columns = get_matrix_dimensions(maze_matrix)
    for i in range(0, rows):
        for j in range(0, columns):
            if maze_matrix[i][j] == 3:
                maze_matrix[i][j] = 1
                final_tile_length = TILE_LENGTH * TILE_SCALE
                tile_center = final_tile_length / 2
                x_len = (j * final_tile_length)
                y_len = (i * final_tile_length)
                x_pos, y_pos = x_len + tile_center, y_len + tile_center
                return pygame.Vector2(x_pos, y_pos)
    return None

def find_player2(pygame, maze_matrix):
    rows, columns = get_matrix_dimensions(maze_matrix)
    for i in range(0, rows):
        for j in range(0, columns):
            if maze_matrix[i][j] == 4:
                maze_matrix[i][j] = 1
                final_tile_length = TILE_LENGTH * TILE_SCALE
                tile_center = final_tile_length / 2
                x_len = (j * final_tile_length)
                y_len = (i * final_tile_length)
                x_pos, y_pos = x_len + tile_center, y_len + tile_center
                return pygame.Vector2(x_pos, y_pos)
    return None

def player_moviment(pygame, dt, player_pos, ):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

