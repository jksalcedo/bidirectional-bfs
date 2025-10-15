# 2D array as gridmap
grid = [[0, 0, 1, 1, 1], # row 0
        [0, 1, 0, 0, 0], # row 1
        [0, 0, 0, 1, 0], # row 2
        [1, 0, 0, 0, 0], # row 3
        [0, 1, 0, 1, 0]] # row 4
# column 0  1  2  3  4

# function to get the neighbors(zeros) of the current node
def get_neighbors(current_node):
    neighbors = []
    row, col = current_node
    possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(grid)
    cols = len(grid[0])

    for dr, dc in possible_moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
            neighbors.append((new_row, new_col))

    return neighbors

def bfs(start, goal):
    queue = [start]
    visited = {start}
    parent = {}

    while queue:
        current_node = queue.pop(0)

        if current_node == goal:
            break # goal found

        for neighbor in get_neighbors(current_node):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)

    if goal not in parent:
        return [start], len(visited)  # no path found

    # reconstruct path
    search_path = []
    current_node = goal
    while current_node in parent:
        search_path.append(current_node)
        current_node = parent[current_node]
    search_path.append(start)
    search_path.reverse()

    return search_path, len(visited)

if __name__ == '__main__':
    start_node = (0, 0)
    goal_node = (4, 4)

    path, length = bfs(start_node, goal_node) # bfs function returns the path and the length of the path

    print("Path:", path)
    print("Visited nodes:", length)

