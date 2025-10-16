from main import get_neighbors

# standard BFS
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