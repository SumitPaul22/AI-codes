def print_board(board):
    for row in board:
        print(" | ".join(row))

def check_winner(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player] * 3 in win_conditions

def minimax(board, player):
    if check_winner(board, 'O'):
        return 1
    if check_winner(board, 'X'):
        return -1
    if all(cell != ' ' for row in board for cell in row):
        return 0

    scores = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = player
                scores.append(minimax(board, 'O' if player == 'X' else 'X'))
                board[i][j] = ' '
    return max(scores) if player == 'O' else min(scores)

def best_move(board):
    # Find the best move for the AI
    best_score = float('-inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 'X')
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def main():
    # Main game loop
    board = [[' ']*3 for _ in range(3)]
    player_turn = True

    while True:
        print_board(board)
        if player_turn:
            cell = int(input("Enter a number (1-9): ")) - 1
            if board[cell // 3][cell % 3] == ' ':
                board[cell // 3][cell % 3] = 'X'
            else:
                print("Cell is already taken!")
                continue
        else:
            x, y = best_move(board)
            board[x][y] = 'O'
            print(f"AI chose: {x * 3 + y + 1}")

        if check_winner(board, 'X'):
            print_board(board)
            print("Congratulations! You've won!")
            break
        if check_winner(board, 'O'):
            print_board(board)
            print("AI wins. Better luck next time!")
            break
        if all(cell != ' ' for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    main()
