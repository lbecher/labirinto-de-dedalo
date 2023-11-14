from player import *
from maze import *

def astar(pygame, maze_matrix):
    # caminho a percorer
    # tupla  [x,y]
    path = []
    end_maze = end_maze(pygame, maze_matrix)
    player_astar = find_player1(pygame, maze_matrix)

    while (end_maze != player_astar):
        if end_maze == player_astar:
            pass
    return path
