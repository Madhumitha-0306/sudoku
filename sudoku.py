def print_board(board):
    print("\n+-------+-------+-------+")
    for i in range(9):
        print("|", end=" ")
        for j in range(9):
            if board[i][j] == 0:
                print(".", end=" ")
            else:
                print(board[i][j], end=" ")

            if (j + 1) % 3 == 0:
                print("|", end=" ")
        print()

        if (i + 1) % 3 == 0:
            print("+-------+-------+-------+")


def is_valid(board, row, col, num):
    # Check row
    for j in range(9):
        if board[row][j] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def is_complete(board):
    for row in board:
        if 0 in row:
            return False
    return True


def sudoku_game():
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],

        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],

        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("================================")
    print("        SUDOKU GAME")
    print("================================")

    print("\nFill the empty cells with numbers from 1 to 9.")
    print("Enter 0 as the row to exit the game.")

    while True:
        print_board(board)

        if is_complete(board):
            print("Congratulations! You completed the Sudoku!")
            break

        try:
            row = int(input("\nEnter row (1-9): "))

            if row == 0:
                print("Game exited. Thank you for playing!")
                break

            col = int(input("Enter column (1-9): "))
            num = int(input("Enter number (1-9): "))

            if row < 1 or row > 9 or col < 1 or col > 9:
                print("Invalid row or column. Please enter values from 1 to 9.")
                continue

            if num < 1 or num > 9:
                print("Invalid number. Please enter a number from 1 to 9.")
                continue

            row -= 1
            col -= 1

            if board[row][col] != 0:
                print("That cell is already filled. Choose another cell.")
                continue

            if is_valid(board, row, col, num):
                board[row][col] = num
                print("Number placed successfully!")
            else:
                print("Invalid move! The number already exists in the row, column, or 3x3 box.")

        except ValueError:
            print("Please enter numbers only.")


sudoku_game()