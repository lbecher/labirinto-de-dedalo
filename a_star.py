from constants import ASTAR_MOV
class AStarNode:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

# função de minimo, verifica o f e escolhe o menor 
def min_value(list):
    min_value = list[0]

    for value in list:
        if value.f < min_value.f:
            min_value = value

    return min_value

# No labirinto o A* não pode andar na diagonal, mas da pra andar a diagonal normamente
def get_movement(teste_movimento):
    if teste_movimento:
        movement = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
    else:
        movement = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return movement

# Permite selecionar qual metodo heuristuico utilizar
def heuristic_calculation(nodo, end_maze, use_manhattan):
    if use_manhattan == True:
        return abs(nodo.position[0] - end_maze.position[0]) + abs(nodo.position[1] - end_maze.position[1])
    else:
        return ((nodo.position[0] - end_maze.position[0]) ** 2) + ((nodo.position[1] - end_maze.position[1]) ** 2)
    

def calculate_a_star(maze_matrix, end_i, end_j, player2_i, player2_j):
    # posição inicial do player e final da matriz
    player_astar = AStarNode(position=(player2_i, player2_j))
    end_maze = AStarNode(position=(end_i, end_j))
    
    # Escolhe forma de percorer percorer os nós adjacentes
    adjacency_choice = False
    movement = get_movement(adjacency_choice)

    # Define se o calculo da heuristica sera por distancia Manhattan ou Euclidiana
    heuristic = True    

    player_astar.g = 0
    player_astar.h = heuristic_calculation(player_astar, end_maze, heuristic)
    player_astar.f = player_astar.g + player_astar.h

    # faça uma lista aberta contendo apenas o nó inicial
    open_list = []
    open_list.append(player_astar)

    # faça uma lista fechada vazia
    closed_list = []
    
    # enquanto o nó de destino não for alcançado
    while open_list:
        # chama função de minimo de f 
        current_node = min_value(open_list)
        open_list.remove(current_node)

        closed_list.append(current_node)

        # se este nó é o nó de destino :
        if current_node == end_maze:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
                # Terminou com SUCESSO
            return path

        else:
            # Verifica os adjacentes da posição atual
            for adjacency in movement:
                # como já existe a posição do nó inicial, calcula a posição x,y do adjacente na matriz
                adjacent_position = (adjacency[0] + current_node.position[0], adjacency[1] + current_node.position[1])

                # Verifica se esta dentro dos limites da matriz em X e Y, verifica se o adjacente não é um obstaculo
                if 0 <= adjacent_position[0] < len(maze_matrix) and 0 <= adjacent_position[1] < len(maze_matrix[0]) and maze_matrix[adjacent_position[0]][adjacent_position[1]] != 0:
                    adjacent_node = AStarNode(position=adjacent_position)
                    adjacent_node.g = current_node.g + 1
                    adjacent_node.h = heuristic_calculation(adjacent_node, end_maze,heuristic)
                    adjacent_node.f = adjacent_node.g + adjacent_node.h

                    # Verifica se algum nó adjacent_node esta na lista fechada
                    in_closed_list = False
                    for node in closed_list:
                        if node == adjacent_node:
                            in_closed_list = True
                            break

                    # Verifica se algum nó adjacent_node esta na lista aberta
                    in_open_list = False
                    for node in open_list:
                        if node == adjacent_node:
                            in_open_list = True
                            break

                    # Se o nó não esta na lista fechada nem na lista aberta
                    if  (in_closed_list == False) and (in_open_list == False):
                        open_list.append(adjacent_node)
                        adjacent_node.parent = current_node

    return None
