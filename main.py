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

if __name__ == '__main__':
    from bfs import bfs
    from bbfs import bidirectional_bfs

    start_node = (1, 2) # row, column
    goal_node = (4, 4)

    path, length = bfs(start_node, goal_node) # bfs function returns the path and the length of the path

    print("BFS Path:", path)
    print("BFS Visited nodes:", length)

    path, length = bidirectional_bfs(start_node, goal_node)  # bidirectional bfs function returns the combined path and the length of the path

    print("Bidirectional BFS Path:", path)
    print("Bidirectional BFS Visited nodes:", length)