import random

# init FASTENED
character = ["O", "X"]


# plaatsen
def place(answerinput):
    global errorName
    indexChar = int(answerinput)
    # check rij 1
    if indexChar < 3:
        # zit in rij 1
        rij_1[indexChar] =  character[player]
    elif indexChar <= 6:
        # rij 2
        rij_2[indexChar-3] =  character[player]
    elif indexChar <= 9:
        # rij 3
        rij_3[indexChar-6] =  character[player]
    else:
        errorName = "List out of Range, "
        MainLoop()
    # checkMate()

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
            if colIndex >= 3:
                # check if this current row is full
                if CurrentRowCount >= 3:
                    # Player has current row filled and won
                    PlayerWin()
                    checkFound = True
                else:
                    CurrentRowCount = 0

                colIndex = 0
                rowIndex += 1
            else:
                colIndex +=1
        
    





# init
board = [
    ["X", "X", "X"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
rij_1 = ["-", "-", "-"]
rij_2 = ["-", "-", "-"]
rij_3 = ["-", "-", "-"]
bot = random.randint(0, 1)
player = 1
# if bot == 0:
#     player = 1
# else:
#     player = 0
errorName = ""
# opposite bot and player random chance.
# this means 0 is a O; and 1 is a X

def MainLoop():
    global errorName
    checkMate()
    print("\n", rij_1, "\n", rij_2, "\n", rij_3)
    try:
        answer = input(f"{errorName}You are {character[player]}, (0-8) where u want to place it? ")
        place(answer)
        errorName = ""
        MainLoop()
    except ValueError:
        errorName = "Value Error, "
        MainLoop()

MainLoop()
    
