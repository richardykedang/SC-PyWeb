from random import randrange
start = [[1, 2, 3], [4, "X", 6], [7, 8, 9]]

def DisplayBoard(board):
    # Mencetak Papan Permainan
    print(("+" + ("-" * 7)) * 3 + "+")
    print(("|" + (" " * 7)) * 3 + "|")
    print("|" + (" " * 3) + str(board[0][0]) + (" " * 3) + "|" + (" " * 3) + str(board[0][1]) + (" " * 3) + "|" + (" " * 3) + str(board[0][2]) + (" " * 3) + "|")
    print(("|" + (" " * 7)) * 3 + "|")
    print(("+" + ("-" * 7)) * 3 + "+")
    print(("|" + (" " * 7)) * 3 + "|")
    print("|" + (" " * 3) + str(board[1][0]) + (" " * 3) + "|" + (" " * 3) + str(board[1][1]) + (" " * 3) + "|" + (" " * 3) + str(board[1][2]) + (" " * 3) + "|")
    print(("|" + (" " * 7)) * 3 + "|")
    print(("+" + ("-" * 7)) * 3 + "+")
    print(("|" + (" " * 7)) * 3 + "|")
    print("|" + (" " * 3) + str(board[2][0]) + (" " * 3) + "|" + (" " * 3) + str(board[2][1]) + (" " * 3) + "|" + (" " * 3) + str(board[2][2]) + (" " * 3) + "|")
    print(("|" + (" " * 7)) * 3 + "|")
    print(("+" + ("-" * 7)) * 3 + "+")

def MakeListOfFreeFields(board):
    free = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            # mencetak row dan column dalam tuple
            if board[i][j] not in ["X", "O"]:
                free.append((i, j))
    return(free)

def VictoryFor(board, sign):
    return((board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or # horizontal
        (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or # horizontal
        (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or # horizontal
        (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or # vertikal
        (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or # vertikal
        (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or # vertikal
        (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or # diagonal
        (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign)) # diagonal


def EnterMove(board):
    free = MakeListOfFreeFields(board)
    move = int(input("Enter your move (1-9)!: "))
    while (((move - 1) // 3, (move - 1) % 3)) not in free:
        print("You cannot choose this potitions!")
        move = int(input("Enter your move (1-9)!: "))
    print("You choose:", move)
    # Update posisi ke papan permainan
    board[(move - 1) // 3][(move - 1) % 3] = "O"

def DrawMove(game):
    free = MakeListOfFreeFields(game)
    move = free[randrange(len(free))]
    while (((move - 1) // 3, (move - 1) % 3)) not in free:
        print("You cannot choose this potitions!")
        move = int(input("Enter your move (1-9)!: "))
    print("You choose:", move)
    # Update posisi ke papan permainan
    game[(move - 1) // 3][(move - 1) % 3] = "X"

#main
game = start[:]
free = MakeListOfFreeFields(game)


print("WELCOME TO TIC-TAC-TOE!\n")
DisplayBoard(game)

while free != []:
    # Pemain melakukan giliran
    EnterMove(game)
    DisplayBoard(game)
    # Cek apakah pemain sudah menang
    if VictoryFor(game, "O") is True:
        print("Game finished, You won!")
        break
    # Komputer melakukan giliran
    DrawMove(game)
    DisplayBoard(game)
    # Cek apakah komputer sudah menang
    if VictoryFor(game, "X") is True:
        print("Game finished, Computer won!")
        break
    free = MakeListOfFreeFields(game)

if free == []:
    print("Game over, You are tied against Computer!")