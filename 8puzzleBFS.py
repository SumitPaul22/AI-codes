from collections import deque
def bfs_solve(start, goal):
    start = tuple(sum(start, []))
    goal = tuple(sum(goal, []))
    queue = deque([(start, 0, [])])
    visited = set()
    moves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
             3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
             6: [3, 7], 7: [4, 6, 8], 8: [5, 7]}

    while queue:
        current, depth, path = queue.popleft()
        if current == goal:
            return depth, path
        if current in visited:
            continue
        visited.add(current)
        zero = current.index(0)
        for move in moves[zero]:
            new_board = list(current)
            new_board[zero], new_board[move] = new_board[move], new_board[zero]
            new_board = tuple(new_board)
            if new_board not in visited:
                queue.append((new_board, depth + 1, path + [new_board]))
    return -1, []

start_board = ([1, 2, 3], [5, 6, 0], [7, 8, 4])
goal_board = ([1, 2, 3], [5, 8, 6], [0, 7, 4])
moves_count, path = bfs_solve(start_board, goal_board)

print(f"Number of moves: {moves_count}")
for step in path:
    print(' '.join(str(num).rjust(2) if num != 0 else '  ' for num in step[:3]))
    print(' '.join(str(num).rjust(2) if num != 0 else '  ' for num in step[3:6]))
    print(' '.join(str(num).rjust(2) if num != 0 else '  ' for num in step[6:]))
    print()
