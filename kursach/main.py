from traverses import GraphTraversal
from actions_on_the_matrix import IncidenceMatrix, Adjacency_list


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find_parent(parent, x)
        y_root = self.find_parent(parent, y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        e = 0
        for i in range(1, len(self.graph)):
            key = self.graph[i]
            j = i - 1
            while j >= 0 and key[2] < self.graph[j][2]:
                self.graph[j + 1] = self.graph[j]
                j -= 1
            self.graph[j + 1] = key

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        i = 0
        while e < self.V - 1 and i < len(self.graph):
            u, v, w = self.graph[i]
            i += 1
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            line = line.replace('\n', '')
            line = line.replace(' ', '')
            matrix.append(list(map(int, line)))

        return matrix


def read_vertices_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        vertices = lines[0].split()
        return vertices


def main():
    filename = 'test.txt'  # замените на имя вашего файла
    with open(filename, 'r') as file:
        data = file.readlines()
        matrix = [list(map(int, line.split())) for line in data[1:]]

    edges = data[0].split()
    num_vertices = len(edges)

    IncidenceMatrix(read_vertices_matrix(filename), read_matrix(filename)).print_incidence_matrix()

    Adjacency_list(read_vertices_matrix(filename), read_matrix(filename)).print_adjacency_list()

    print('Матрица смежности:')
    m = read_matrix(filename)
    for i in range(len(m)):
        for x in m:
            print(x[i], end=' ')
        print()

    g = Graph(num_vertices)

    for i in range(1, num_vertices + 1):
        weights = list(map(int, data[i].split()))
        for j in range(num_vertices):
            if weights[j] != 0:
                g.add_edge(i - 1, j, weights[j])

    result = g.kruskal()
    print('Алгоритм Краскала')
    for u, v, weight in result:
        print(f"{edges[u]} {edges[v]}")
    print(sum(weights))

    graph_traversal_obj = GraphTraversal(Adjacency_list(read_vertices_matrix(filename), read_matrix(filename)).create_adjacency_list())
    print("Обход в ширину:")
    print(graph_traversal_obj.iterative_dfs('A'))
    print("\nОбход в глубину:")
    print(graph_traversal_obj.bfs('A'))


if __name__ == "__main__":
    main()
