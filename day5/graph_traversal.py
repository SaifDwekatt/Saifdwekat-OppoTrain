from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, src, dest):
        if src not in self.adj:
            self.adj[src] = []
        if dest not in self.adj:
            self.adj[dest] = []
        self.adj[src].append(dest)
        self.adj[dest].append(src)  # Undirected

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                result.append(node)
                for neighbor in self.adj[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return result

    def dfs(self, start):
        visited = set()
        result = []

        def _dfs(v):
            visited.add(v)
            result.append(v)
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return result

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    print("BFS:", g.bfs('A'))
    print("DFS:", g.dfs('A'))
