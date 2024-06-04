import heapq

import matrizbinaria as mtbinaria
import transforma_cinza as cinza
from pixelazul import pixel_azul as rota

class Node:
    def __init__(self, row, col, parent=None):
        self.row = row
        self.col = col
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f


def heuristic(node, goal):
    distancia = abs(node.row - goal.row) + abs(node.col - goal.col)
    return distancia


def astar(matrix, start, goal):
    rows = len(matrix)
    cols = len(matrix[0])
    open_list = []
    closed_set = set()
    visited_nodes = []

    start_node = Node(start[0], start[1])
    goal_node = Node(goal[0], goal[1])

    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.row == goal_node.row and current_node.col == goal_node.col:
            path = []
            while current_node is not None:
                path.append((current_node.row, current_node.col))
                current_node = current_node.parent
            return path[::-1], visited_nodes

        closed_set.add((current_node.row, current_node.col))
        visited_nodes.append((current_node.row, current_node.col))

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_row, new_col = (current_node.row + i, current_node.col + j)

            if 0 <= new_row < rows and 0 <= new_col < cols and matrix[new_row][new_col] == 1 and (
                    new_row, new_col) not in closed_set:
                new_node = Node(new_row, new_col, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_node, goal_node)
                new_node.f = new_node.g + new_node.h
                heapq.heappush(open_list, new_node)
                closed_set.add((new_row, new_col))

    return None, visited_nodes

caminho = input(r"Digite o caminho da imagem com os pontos coloridos: ").strip(' " ')
#caminho = r"C:\Users\gustavo\Desktop\ATUAL.png"
img_cinza, indexpartida, indexchegada = cinza.transforma_cinza(caminho)
matriz = mtbinaria.transforma_matriz(caminho)

heuristica_cod2, vs = astar(matriz, indexpartida, indexchegada)

rota(heuristica_cod2, caminho)
print(f"Partida:", indexpartida)
print(f"Chegada:", indexchegada)

print("Melhor caminho:", heuristica_cod2)

