from collections import deque

# -------------------------------
# Define the graph as an adjacency list
# -------------------------------
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# -------------------------------
# Depth First Search (DFS) - Recursive
# -------------------------------
def dfs_recursive(graph, node, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    print(node, end=' ')  # Process the current node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# -------------------------------
# DFS Wrapper for Disconnected Graphs
# -------------------------------
def dfs_all(graph):
    visited = set()
    for node in graph:
        if node not in visited:
            dfs_recursive(graph, node, visited)

# -------------------------------
# Breadth First Search (BFS) - Iterative
# -------------------------------
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            # Add unvisited neighbors to the queue
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# -------------------------------
# Main function to run DFS and BFS
# -------------------------------
def main():
    print("DFS (recursive):")
    dfs_recursive(graph, 'A')  # or use dfs_all(graph) for disconnected graphs
    print("\nBFS (iterative):")
    bfs(graph, 'A')

# -------------------------------
# Entry point
# -------------------------------
if __name__ == "__main__":
    main()
