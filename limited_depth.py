def busca_profundidade_limitada(labirinto, posicao_atual, limite, caminho_atual=[], visitadas=set()):
    lin, col = posicao_atual

    if limite < 0:
        return None  # Limite atingido, não há caminho

    if labirinto[lin][col] == 2:
        # Encontrou a saída
        caminho_atual.append(posicao_atual)
        return caminho_atual

    if labirinto[lin][col] == 0 or posicao_atual in visitadas:
        return None  # Parede ou posição já visitada

    visitadas.add(posicao_atual)
    caminho_atual.append(posicao_atual)

    # Passa o labirinto como parâmetro para a função obter_vizinhos
    vizinhos = obter_vizinhos(labirinto, posicao_atual)
    for vizinho in vizinhos:
        resultado = busca_profundidade_limitada(labirinto, vizinho, limite - 1, caminho_atual, visitadas)
        if resultado:
            return resultado

    # Se nenhum caminho foi encontrado, remove a posição atual das visitadas
    visitadas.remove(posicao_atual)
    return None  # Caminho não encontrado neste ramo


# Restante do código...
def obter_vizinhos(labirinto, posicao):
    lin, col = posicao
    vizinhos = []

    # Verifica para cima
    if lin > 0:
        vizinhos.append((lin - 1, col))
    # Verifica para baixo
    if lin < len(labirinto) - 1:
        vizinhos.append((lin + 1, col))
    # Verifica à esquerda
    if col > 0:
        vizinhos.append((lin, col - 1))
    # Verifica à direita
    if col < len(labirinto[0]) - 1:
        vizinhos.append((lin, col + 1))

    return vizinhos

# Exemplo de uso
def calculate_limited_depth(maze_matrix, end_i, end_j, player2_i, player2_j):
    limite_exemplo = 30

    caminho_encontrado = busca_profundidade_limitada(maze_matrix, (player2_i, player2_j), limite_exemplo)
    while caminho_encontrado is None:
        print("Tentando novamente...")
        limite_exemplo += 1
        caminho_encontrado = busca_profundidade_limitada(maze_matrix, (player2_i, player2_j), limite_exemplo)

    if caminho_encontrado:
        print("Caminho encontrado:", caminho_encontrado)
    else:
        print("Nenhum caminho encontrado mesmo após várias tentativas.")

    caminho_encontrado.reverse()
    
    return caminho_encontrado