import random
# Board Size
boardSize = 4

# Display function
def display():
    ## Identify the largest value
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    numSpace = len(str(largest))
    
    for row in board:
        currRow = "|"
        for element in row:
            if element == 0:
                currRow += " " * numSpace + "|"
            else:
                currRow += (" " * (numSpace - len(str(element)))) + str(element) + "|"
        print(currRow)
    print()

def mergeOneRowL(row):
    for i in range(boardSize - 1):
        for j in range(boardSize - 1, 0, -1):
            if row[j - 1] == 0:
                row[j - 1] = row[j]
                row[j] = 0

    for i in range(boardSize - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0

    for i in range(boardSize - 1, 0, -1):
        if row[i - 1] == 0:
            row[i - 1] = row[i]
            row[i] = 0
    return row

def merge_left(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = mergeOneRowL(currentBoard[i])
    return currentBoard

def reverse(row):
    new = []
    for i in range(boardSize -1, -1, -1):
        new.append(row[i])
    return new


def merge_right(currentBoard):
    for i in range(boardSize):
        currentBoard[i] = reverse(currentBoard[i])
        currentBoard[i] = mergeOneRowL(currentBoard[i])
        currentBoard[i] = reverse(currentBoard[i])
    return currentBoard

def transpose(currentBoard):
    for j in range(boardSize):
        for i in range(j, boardSize):
            if not i == j:
                temp = currentBoard[j][i]
                currentBoard[j][i] = currentBoard[i][j]
                currentBoard[i][j] = temp
    return currentBoard

def merge_up(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_left(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def merge_down(currentBoard):
    currentBoard = transpose(currentBoard)
    currentBoard = merge_right(currentBoard)
    currentBoard = transpose(currentBoard)
    return currentBoard

def pickNewValue():
    if random.randint(1, 8) == 1:
            return 4
    else:
        return 2
    
    
board = []
for i in range(boardSize):
    row = []
    for j in range(boardSize):
        row.append(0)
    board.append(row)

numNeeded = 2
while numNeeded > 0:
    rowNum = random.randint(0, boardSize - 1)
    colNum = random.randint(0, boardSize - 1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = pickNewValue()
        numNeeded -= 1

print("Welcome to 2048")
display()

gameOver = False

while not gameOver:
    move = input("Which way you want to merge :- ")
    
    validInput = True
    
    if move == 'd':
        board = merge_right(board)
    elif move == 'w':
        board = merge_up(board)
    elif move == 'a':
        board = merge_left(board)
    elif move == 's':
        board = merge_down(board)
    else:
        validInput = False
        
    if not validInput:
        print("Invalid input try again")
    else:
        display()
    
    
    