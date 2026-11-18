import random

# init FASTENED
character = ["O", "X"]
gameLoop = True
winning_positions = (
    # Horizontal
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),

    # Vertical
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),

    # Diagonal
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0))
)


# calculate placement
def place_cal(pickedNumber):
    if pickedNumber < 3:
        # Row 1
        return 0, (pickedNumber)
    elif pickedNumber <= 6:
        # Row 2
        return 1, (pickedNumber-1)
    elif pickedNumber <= 8:
        # row 3
        return 2, (pickedNumber-2)
    else:
        return None

# placing
def place(answerinput):
    global errorName
    indexChar = int(answerinput)

    inputNum = place_cal(indexChar)
    if not indexChar > 8:
        board[inputNum[0]][inputNum[1]] = character[player]
    else:
        errorName = "List out of Range, "

def PlayerWin():
    global gameLoop
    print("player has won")
    gameLoop = False

def BotWin():
    global gameLoop
    print("bot has won")
    gameLoop = False

def checkMate():
    # lets pick 1 by 1 a number
    for i in range (8):
        # lets pick a winning position
        first, second, third = winning_positions[i]

        # now we have 3 winning positions. lets check wheater they match
        if board[first[0]][first[1]] == board[second[0]][second[1]] == board[third[0]][third[1]]:
            # so now in these 3 cord we have also 3 the same value. lets check wheater they are the player or not.
            if board[first[0]][first[1]] == character[player]:
                # player match he won
                PlayerWin()
            elif board[first[0]][first[1]] == character[bot]:
                # bot has won
                BotWin()
            else:
                # prob -. means nobody won. skip
                continue



# init
board = [
    ["X", "X", "X"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
bot = random.randint(0, 1)
player = 1
# if bot == 0:
#     player = 1
# else:
#     player = 0
errorName = ""
# opposite bot and player random chance.
# this means 0 is a O; and 1 is a X

def ShowBoard():
    for i in range(3):
        colNumber = i
        for i in range(3):
            ShowRow = board[colNumber][i]
        print(ShowRow)

def MainLoop():
    while gameLoop:
        global errorName
        checkMate()
        ShowBoard()
        try:
            answer = int(input(f"{errorName}You are {character[player]}, (0-8) where u want to place it? "))

            # - is - not X or O (player, Bot)
            calResult = place_cal(answer)
            if board[calResult[0]][calResult[1]] != character[player] and board[calResult[0]][calResult[1]] != character[bot]:
                place(answer)
                errorName = ""
                
            else:
                errorName = "Already ocuppied, "
        except ValueError:
            errorName = "Value Error, "

MainLoop()
    
