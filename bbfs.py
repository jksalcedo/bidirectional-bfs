# this runs two BFS searches that meet in the middle
from main import get_neighbors


def bidirectional_bfs(start, goal):
    # forward
    queue_f = [start]
    visited_f = {start}
    parent_f = {}

    # backward
    queue_b = [goal]
    visited_b = {goal}
    parent_b = {}

    meeting_point = None

    while queue_f and queue_b:
        # --- FORWARD SEARCH ---
        current_f = queue_f.pop(0)
        neighbors_f = get_neighbors(current_f)

        for neighbor in neighbors_f:
            if neighbor not in visited_f:
                visited_f.add(neighbor)
                queue_f.append(neighbor)
                parent_f[neighbor] = current_f

                #check for meeting point when a neighbor is discovered
                if neighbor in visited_b:
                    meeting_point = neighbor
                    break  # Exit the neighbor loop

        if meeting_point:
            break  # Exit the main while loop

        # --- BACKWARD SEARCH ---
        current_b = queue_b.pop(0)
        neighbors_b = get_neighbors(current_b)

        for neighbor in neighbors_b:
            if neighbor not in visited_b:
                visited_b.add(neighbor)
                queue_b.append(neighbor)
                parent_b[neighbor] = current_b

                if neighbor in visited_f:
                    meeting_point = neighbor
                    break  # Exit the neighbor loop

        if meeting_point:
            break  # exit the main while loop

    # no path was found
    if not meeting_point:
        return None, len(visited_f) + len(visited_b)

    # reconstruct path
    path_f = []
    node = meeting_point
    while node in parent_f:
        path_f.append(node)
        node = parent_f[node]
    path_f.append(start)
    path_f.reverse()

    path_b = []
    node = meeting_point
    while node in parent_b:
        # the first node is the meeting_point, which is already in path_f
        # so we don't append it here until after the loop
        node = parent_b[node]
        path_b.append(node)

    final_path = path_f + path_b

    return final_path, len(visited_f) + len(visited_b)