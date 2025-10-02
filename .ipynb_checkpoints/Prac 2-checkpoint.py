import heapq

# Define the grid: 0 = free path, 1 = wall
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

# Heuristic function: Manhattan distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* Algorithm
def astar(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (heuristic(start, goal), 0, start, [start]))
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x, y = current[0] + dx, current[1] + dy
            next_node = (x, y)

            if 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0:
                if next_node not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic(next_node, goal)
                    heapq.heappush(open_set, (new_f, new_g, next_node, path + [next_node]))

    return None

# Run the algorithm
path = astar(maze, start, goal)

# Output the result
if path:
    print("A* Path:", path)

    # Optional: visualize the path in the maze
    maze_path = [row[:] for row in maze]  # Copy maze
    for x, y in path:
        maze_path[x][y] = '*'
    print("\nMaze with path:")
    for row in maze_path:
        print(' '.join(str(cell) if cell != '*' else '*' for cell in row))
else:
    print("No path found.")
