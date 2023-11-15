from player import *
from maze import *

# inicia os valores de g,h,f & define posição e parent
def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

def __eq__(self, other):
    return self.position == other.position

def astar(pygame, maze_matrix):
    # maze setup
    maze_matrix_search = load_maze_matrix()

    # posição inicial do player para calcula do nó
    player_astar = find_player1(pygame, maze_matrix)
    player_astar.g = 0
    player_astar.h = 0
    player_astar.f = 0

    # posição final do labirinto para o calculo do nó
    end_maze = find_maze_end(pygame, maze_matrix)
    end_maze.g = 0
    end_maze.h = 0
    end_maze.f = 0

    # cria lista aberta e lista fechada
    open_list = []
    closed_list = []

    # Adiciona a lista a posção inicial do player A*
    open_list.append(player_astar)

    # Laço enquanto não achar o final, len pega o comprimento total da lista
    while len(open_list) > 0:
        #pega a posição atual na lista
        current_position = open_list[0]
        #inicializa com 0 o indice atual
        current_index = 0
        # utiliza enumerate para para obter o valor e o indice
        for index, item in enumerate(open_list):
            # verifica se o custo total de da posição inicial é menor que a final
            if item.f < current_position.f:
                current_position = item
                current_index = index

        # adiciona mais um item a lista a lista aberta, o novo melhor valor
        # a lista fechada resebe a nova melher posição 
        open_list.pop(current_index)
        closed_list.append(current_position)

        # verifica se a posição atual é a posição destino
        if current_position == end_maze:
            # inicia lista do caminho
            path = []
            # cria uma variavel para evitar que mudanças na execução alterem a lista
            current = current_position

            # percore o laço enquanto não for vazio
            while current is not None:
                path.append(current.position)
                current = current.parent
                # inverte a lista para retornala
                return list(reversed(path))

        # posição atual não é destino
        else:
            # lista para vizinhos 
            neighborhood = []
            
            # laço que tenta gerar vizinhos nas 8 posições adjasentes 
            for new_position in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                # posição atual do player somando o valor atual com o deslocamento
                player_position = (current_position.postion[0] + new_position[0], current_position.position[1] + new_position[1])

                # verifica se esta nas proximidades do player
                if (player_position[0] > (len(maze_matrix_search) - 1) 
                    or player_position[0] < 0 
                    or player_position[1] > (len(maze_matrix_search[0]) - 1)  # Ajuste aqui
                    or player_position[1] < 0):
                    continue

                # verifica se é possivel percorrer essa posição da matriz
                if maze_matrix_search[player_position[0]][player_position[1]] != 1:
                    continue

                # nova posição possivel
                next_position = (current_position, player_position)

                # adiciona a posição na lista de visinhos
                neighborhood.append(next_position)

            # Procura em toda visinhaça
            for neighbor in neighborhood:
                # visinhos que estão na lista fechada
                for closed_neighbor in closed_list:
                    if neighbor == closed_neighbor:
                        continue

                # Calcula os valores de f, g, h
                neighbor.g = current_position.g +1
                neighbor.h = ((neighbor.position[0] - end_maze.position[0]) ** 2)
                neighbor.f = neighbor.g + neighbor.h

                # se o caminho esta na lista e o caminho é maior que o onterior, o visinho não e adicionado na lista
                for open_position in open_list:
                    if neighbor == open_position and neighbor.g > open_position:
                        continue

                # coloca visinho na lista aberta
                open_list.append(neighbor)