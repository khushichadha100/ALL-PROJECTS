import math

EMPTY = ' '
user_move=input("choose your mark : (X/O): ")
if user_move == "X" or user_move == "x":
    print("ok ! you = X , me = O")
    PLAYER_X = 'X'
    PLAYER_O = 'O'
elif user_move == "O" or user_move == "o" :
    print("ok ! you = O , me = X")
    PLAYER_X = 'O'
    PLAYER_O = 'X'
else :
    print("invalid mark !")

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('---' * 5)

def check_winner(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]
    return [player] * 3 in win_conditions

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def minimax(board, depth, is_maximizing):
    if check_winner(board, PLAYER_X):
        return -10
    if check_winner(board, PLAYER_O):
        return 10
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_O
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

def play_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    print("Tic-Tac-Toe Game\n")
    print_board(board)

    while True:
        # Player X Move
        while True:
            try:
                x, y = map(int, input("Enter row and column for X (0, 1, 2): ").split())
                if board[x][y] == EMPTY:
                    board[x][y] = PLAYER_X
                    break
                else:
                    print("Cell is taken. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Try again.")

        print_board(board)
        if check_winner(board, PLAYER_X):
            print("Player X wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break
        

        # Computer Move
        print("Computer is making a move...")
        move = get_best_move(board)
        if move:
            board[move[0]][move[1]] = PLAYER_O
        print_board(board)
        if check_winner(board, PLAYER_O):
            print("Player O (Computer) wins!")
            break
        if is_full(board):
            print("It's a draw!")
            break

# Run the game
play_game()
