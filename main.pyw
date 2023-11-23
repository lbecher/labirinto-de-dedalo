import pygame

from game_mode import *
from player import *
from maze import *

from a_star import calculate_a_star
from limited_depth import calculate_limited_depth

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
#player1_i, player1_j = 0, 2
#player2_i, player2_j = 0, 4
player1_i, player1_j = find_player1(maze_matrix, maze_rows, maze_columns)
player2_i, player2_j = find_player2(maze_matrix, maze_rows, maze_columns)
#end_i, end_j = 4, 2
end_i, end_j = find_maze_end(maze_matrix, maze_rows, maze_columns)

# se usar IA, calcular rotas de cada player
player1_movement_stack = calculate_limited_depth(maze_matrix, end_i, end_j, player1_i, player1_j)
player2_movement_stack = calculate_a_star(maze_matrix, end_i, end_j, player2_i, player2_j)

# loop principal do jogo
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

    # movementa players
    if True:
        (player1_i, player1_j) = player1_movement_stack.pop()
        player1_pygame_coordinates = maze_to_pygame_coordinates(player1_i, player1_j)

        #(player2_i, player2_j) = player2_movement_stack.pop()
        #player2_pygame_coordinates = maze_to_pygame_coordinates(player2_i, player2_j)
    else:
        player1_i, player1_j = player1_keyboard_movement(maze_matrix, maze_rows, maze_columns, player1_i, player1_j)
        player1_pygame_coordinates = maze_to_pygame_coordinates(player1_i, player1_j)

        player2_i, player2_j = player2_keyboard_movement(maze_matrix, maze_rows, maze_columns, player2_i, player2_j)
        player2_pygame_coordinates = maze_to_pygame_coordinates(player2_i, player2_j)
    
    # desenha players
    pygame.draw.circle(screen, "red", player1_pygame_coordinates, 32)
    #pygame.draw.circle(screen, "blue", player2_pygame_coordinates, 32)

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(5) / 1000

pygame.quit()
