import random

def main():
    player = change_player_turn("")
    board = create_board()
    # print("Player X turn") if random_player == 0 else print("Player O turn")
    # random_player = random_player_turn()
    while not (winner(board) or draw(board)):
        display_board(board)
        
        print()
        
        make_turn(player,board)
        player = change_player_turn(player)
        
        
    display_board(board)
    print("Good game!")

    


def create_board():
    board = []
    for i in range (9):
        board.append(i +1)
    return board

def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print()
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print()
    print(f"{board[6]} | {board[7]} | {board[8]}")

def winner(board):
    return(board[0] == board[3] == board[6] or 
    board[1] == board[4] == board[7] or 
    board[2] == board[5] == board[8] or 
    board[0] == board[1] == board[2] or
    board[3] == board[4] == board[5] or
    board[6] == board[7] == board[8] or 
    board[6] == board[4] == board[2] or 
    board[0] == board[4] == board[8])

def draw(board):
    for i in range(9):
        if board[i] != "X" or board[i] != "O":
            return False
    return True

    

# def random_player_turn():
#     return random.randint(0, 1)

def change_player_turn(current):
    if current == "" or current == "O":
        return "X"
    elif current == "X":
        return "O"


def make_turn(player, board):
    turn = int(input(f"{player} choose a number between 1-9: "))
    board[turn - 1] = player


if __name__ == "__main__":
    main()
