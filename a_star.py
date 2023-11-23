from player import *
from maze import *

# inicia os valores de g,h,f & define posição e parent
class AStarCell:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other

def calculate_a_star(maze_matrix, end_i, end_j, player2_i, player2_j):
    # posição inicial do player para calcula do nó
    player_astar = AStarCell(position=(player2_i, player2_j))
    player_astar.g = 0
    player_astar.h = 0
    player_astar.f = 0

    # posição final do labirinto para o calculo do nó
    end_maze = AStarCell(position=(end_i, end_j))
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
            for i in open_list:
                path.append(i.position)
            return path
            '''
            path = []
            # cria uma variavel para evitar que mudanças na execução alterem a lista
            current = current_position

            # percore o laço enquanto não for vazio
            while current is not None:
                path.append(current.position)
                current = current.parent
                # inverte a lista para retornala
                print("A*=")
                print(path)
                return list(reversed(path))'''

        # posição atual não é destino
        else:
            # lista para vizinhos 
            neighborhood = []
            
            # laço que tenta gerar vizinhos nas 8 posições adjasentes 
            for new_position in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                # posição atual do player somando o valor atual com o deslocamento
                #player_position = (current_position.position[0] + new_position[0], current_position.position[1] + new_position[1])

                if current_position.position is not None:
                    player_position = (current_position.position[0] + new_position[0], current_position.position[1] + new_position[1])
                else:
                    continue
                # verifica se esta nas proximidades do player
                if (player_position[0] > (len(maze_matrix) - 1) 
                    or player_position[0] < 0 
                    or player_position[1] > (len(maze_matrix[0]) - 1)  # Ajuste aqui
                    or player_position[1] < 0):
                    continue

                # verifica se é possivel percorrer essa posição da matriz
                if maze_matrix[player_position[0]][player_position[1]] != 1:
                    continue

                # nova posição possivel
                next_position = (current_position, player_position)

                sla = AStarCell(parent=current_position)

                # adiciona a posição na lista de visinhos
                neighborhood.append(sla)

            # Procura em toda vizinhança
            for neighbor in neighborhood:
                # vizinhos que estão na lista fechada
                if neighbor in closed_list:
                    continue

                # Calcula os valores de f, g, h
                neighbor.g = current_position.g + 1
                if neighbor.position is not None and end_maze.position is not None:
                    neighbor.h = ((neighbor.position[0] - end_maze.position[0]) ** 2)
                else:
                    neighbor.h = 0  
                #neighbor.h = ((neighbor.position[0] - end_maze.position[0]) ** 2)
                neighbor.f = neighbor.g + neighbor.h

                # se o caminho está na lista e o caminho é maior que o anterior, o vizinho não é adicionado na lista
                if neighbor in open_list and neighbor.g > open_list[open_list.index(neighbor)].g:
                    continue

                # coloca vizinho na lista aberta
                open_list.append(neighbor)
    
    return None