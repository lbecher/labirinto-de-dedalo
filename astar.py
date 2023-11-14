from player import *
from maze import *

# inicia visinho, a posição e os valores de g,h,f
def __init__(self, neighbor=None, position=None):
        self.neighbor = neighbor
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

def __eq__(self, other):
    return self.position == other.position

def astar(pygame, maze_matrix):
    # posição inicial do player para calcula do nó
    player_astar = find_player1(pygame, maze_matrix)
    player_astar.g = 0
    player_astar.h = 0
    player_astar.f = 0

    # posição final do labirinto para o calculo do nó
    end_maze = end_maze(pygame, maze_matrix)
    end_maze.g = 0
    end_maze.h = 0
    end_maze.f = 0

    # cria lista aberta e lista fechada
    open_list = []
    closed_list = []

    # Adiciona a lista a posção inicial do player A*
    open_list.append(player_astar)

    while (end_maze != player_astar):
        if end_maze == player_astar:
            pass
    return 0
