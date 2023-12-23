#from deque import Deque as deque
from collections import deque


class GraphTraversal:
    def __init__(self, graph):
        self.graph = graph
        self.visited = set()

    def iterative_dfs(self, start):
        path = []
        stack = [start]

        while stack:
            v = stack.pop()
            if v not in self.visited:
                path.append(v)
                self.visited.add(v)
                stack.extend([node for node in self.graph[v] if node not in self.visited])
        return path

    def bfs(self, start_node):
        visited = []
        queue = deque([start_node])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.append(vertex)
                queue.extend(set(self.graph[vertex]) - set(visited))
        return visited
'''
class GraphTraversal:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def breadth_first_search(self, start_vertex):
        visited = {vertex: False for vertex in self.adjacency_list}
        queue = deque([start_vertex])
        visited[start_vertex] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)

            for neighbor in self.adjacency_list[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def depth_first_search(self, start_vertex):
        visited = {vertex: False for vertex in self.adjacency_list}

        def dfs_recursive(vertex):
            print(vertex)
            visited[vertex] = True
            for neighbor in self.adjacency_list[vertex]:
                if not visited[neighbor]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)
'''