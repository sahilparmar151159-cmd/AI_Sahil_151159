#NAME : DEVENDRA ODEDARA
#ENO: 92600584011

def display(board):
    print()
    print(board[0],"|",board[1],"|",board[2])
    print("--+---+--")
    print(board[3],"|",board[4],"|",board[5])
    print("--+---+--")
    print(board[6],"|",board[7],"|",board[8])
    print()
    
def heuristic(board):
    win = [
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (0,4,8),
        (2,4,6)
        
    ]
    
    for a,b,c in win:
        if board[a] == board[b] == board[c] == "x":
            return 10
        if board[a] == board[b] == board[c] == "O":
            return -10

    return 0

board = [" "] * 9
player = "x"

for turn in range(9):
    display(board)
    print("player",player)
    
    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue

    board[pos] = player

    score = heuristic(board)
    if score == 10:
        display(board)
        print("Player x wins!")
        break

    if score == -10:
        display(board)
        print("Player O wins!")
        break

    if player == "x":
        player = "O"
    else:
        player = "x"

else:
    display(board)
    print("Match Draw!")



