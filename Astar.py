from heapq import heappush, heappop

# Simplified A* algorithm
def a_star_algorithm(start, end, adjacency_list, heuristic):
    open_list = [(0 + heuristic(start), 0, start, [start])]
    closed_set = set()

    while open_list:
        _, cost, node, path = heappop(open_list)

        if node in closed_set:
            continue

        if node == end:
            return path, cost

        closed_set.add(node)

        for neighbor, weight in adjacency_list.get(node, []):
            if neighbor not in closed_set:
                heappush(open_list, (cost + weight + heuristic(neighbor), cost + weight, neighbor, path + [neighbor]))

    return None, None

# Example usage:
adjacency_list = {
    'A': [('B', 1), ('I', 5), ('J', 3)],
    'B': [('C', 2), ('D', 4)],
    'C': [],
    'D': [('E', 1), ('F', 2), ('G', 3)],
    'E': [('H', 2)],
    'F': [],
    'G': [],
    'H': [],
    'I': [],
    'J': []
}

# Heuristic function for A*
def h(n):
    H = {
        'A': 0,
        'B': 7,
        'C': 5,
        'D': 3,
        'E': 2,
        'F': 2,
        'G': 3,
        'H': 0,
        'I': 11,
        'J': 15
    }
    return H[n]

# Call the simplified A* algorithm
path, cost = a_star_algorithm('A', 'H', adjacency_list, h)
print('Path found:',path)
print('Total cost:',cost)
