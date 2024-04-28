class Graph:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]
        print(stack)
        while stack:
            (node, path) = stack.pop()
            print((node, path))
            if node not in visited:
                visited.add(node)
                print(visited)
                if node == goal:
                    return path
                for neighbor in self.graph[node]:
                    stack.append((neighbor, path + [neighbor]))
                    print(stack)
        return None

# Example usage:
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    g = Graph(graph)
    start_node = 'A'
    goal_node = 'F'
    path = g.dfs(start_node, goal_node)
    if path:
        print(f"Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No path found from {start_node} to {goal_node}")
