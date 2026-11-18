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
        return 0, (pickedNumber-1)
    elif pickedNumber <= 6:
        # Row 2
        return 1, (pickedNumber-4)
    elif pickedNumber <= 8:
        # row 3
        return 2, (pickedNumber-7)
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
    print("player has won")

def BotWin():
    print("bot has won")

def checkMate():
    CurrentRowCount = 0
    rowIndex = 0
    colIndex = 0
    checkFound = False
    # row check
    while not checkFound:
        if board[rowIndex][colIndex] == character[player]:
            CurrentRowCount +=1
            if colIndex >= 2:
                # check if this current row is full
                if CurrentRowCount >= 3:
                    # Player has current row filled and won
                    PlayerWin()
                    checkFound = True
                else:
                    CurrentRowCount = 0
                    checkFound = True

                colIndex = 0
                rowIndex += 1
            else:
                colIndex +=1
        else:
            # so player  
        
    


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
    rowNumber = 0
    for i in range(3):
        for i in range(3):
            print(board[rowNumber][i])
        rowNumber +=1

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
    
