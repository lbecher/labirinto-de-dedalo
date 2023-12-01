import math

class AStarNode:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

def calcula_aStar(maze_matrix, end_i, end_j, player2_i, player2_j):
    # posição inicial do player e final da matriz
    player_astar = AStarNode(position=(player2_i, player2_j))
    end_maze = AStarNode(position=(end_i, end_j))

    player_astar.g = 0
    # formula para calcular a distancia Manhattan
    player_astar.h = abs(player_astar.position[0] - end_maze.position[0]) + abs(player_astar.position[1] - end_maze.position[1])
    player_astar.f = player_astar.g + player_astar.h

    # faça uma lista aberta contendo apenas o nó inicial
    open_list = []
    open_list.append(player_astar)

    # faça uma lista fechada vazia
    closed_list = []
    
    # enquanto o nó de destino não for alcançado
    while open_list:
        current_node = min(open_list, key=lambda x: x.f)
        open_list.remove(current_node)

        closed_list.append(current_node)

        if current_node == end_maze:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path

        neighborhood = []

        # Exeção a regra do A* para que não se possa andar na diagonal no labirinto
        teste_movimento = False
        if teste_movimento == True:
            movement = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        else:
            movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for adjacency in movement:
            adjacent_position = (adjacency[0] + current_node.position[0], adjacency[1] + current_node.position[1])

            if 0 <= adjacent_position[0] < len(maze_matrix) and 0 <= adjacent_position[1] < len(maze_matrix[0]) and maze_matrix[adjacent_position[0]][adjacent_position[1]] != 0:
                adjacent_node = AStarNode(position=adjacent_position)
                adjacent_node.g = current_node.g + 1
                adjacent_node.h = abs(adjacent_node.position[0] - end_maze.position[0]) + abs (adjacent_node.position[1] - end_maze.position[1])
                adjacent_node.f = adjacent_node.g + adjacent_node.h

                in_closed_list = any(node == adjacent_node for node in closed_list)
                in_open_list = any(node == adjacent_node for node in open_list)

                if not in_closed_list and not in_open_list:
                    open_list.append(adjacent_node)
                    adjacent_node.parent = current_node

    return None
