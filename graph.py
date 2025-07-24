from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex in self.adj:
            print(f"Vertex {vertex} already exists.")
        else:
            self.adj[vertex] = []
            print(f"Vertex {vertex} added.")

    def add_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            print("One or both vertices not found.")
            return
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if u not in self.adj[v]:
            self.adj[v].append(u)
        print(f"Edge between {u} and {v} added.")

    def remove_edge(self, u, v):
        if u in self.adj and v in self.adj[u]:
            self.adj[u].remove(v)
        if v in self.adj and u in self.adj[v]:
            self.adj[v].remove(u)
        print(f"Edge between {u} and {v} removed.")

    def remove_vertex(self, vertex):
        if vertex not in self.adj:
            print(f"Vertex {vertex} not found.")
            return
        for neighbor in self.adj[vertex]:
            self.adj[neighbor].remove(vertex)
        del self.adj[vertex]
        print(f"Vertex {vertex} removed.")

    def display(self):
        if not self.adj:
            print("Graph is empty.")
        else:
            print("Graph adjacency list:")
            for vertex in self.adj:
                print(f"{vertex}: {self.adj[vertex]}")

    def dfs(self, start):
        if start not in self.adj:
            print("Start vertex not found.")
            return
        visited = set()
        result = []

        def _dfs(v):
            visited.add(v)
            result.append(v)
            for neighbor in self.adj[v]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        print("DFS traversal:", result)

    def bfs(self, start):
        if start not in self.adj:
            print("Start vertex not found.")
            return
        visited = set()
        queue = deque([start])
        result = []

        while queue:
            v = queue.popleft()
            if v not in visited:
                visited.add(v)
                result.append(v)
                for neighbor in self.adj[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        print("BFS traversal:", result)


def main():
    g = Graph()
    while True:
        print("\n1. Add Vertex")
        print("2. Add Edge")
        print("3. Remove Edge")
        print("4. Remove Vertex")
        print("5. Display Graph")
        print("6. DFS")
        print("7. BFS")
        print("0. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            v = input("Enter vertex: ")
            g.add_vertex(v)
        elif choice == '2':
            u = input("Enter first vertex: ")
            v = input("Enter second vertex: ")
            g.add_edge(u, v)
        elif choice == '3':
            u = input("Enter first vertex: ")
            v = input("Enter second vertex: ")
            g.remove_edge(u, v)
        elif choice == '4':
            v = input("Enter vertex to remove: ")
            g.remove_vertex(v)
        elif choice == '5':
            g.display()
        elif choice == '6':
            start = input("Enter start vertex for DFS: ")
            g.dfs(start)
        elif choice == '7':
            start = input("Enter start vertex for BFS: ")
            g.bfs(start)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

main()
