"""
This program will input the user for the length of a square and its value.
Afterwards, the program will check if the given square is a magic square.
Foundation provided by Ms. Richardson
Edits made by Justin
Information provided by Wikipedia
"""

# This procedure prompts the user for n^2 inputs to populate a
# 2D square array which has alreay been declared
# precondition:  sqArr has been declared with a size of nxn
def fillSquare(n, sqArr):
    for r in range(n):
        print("----ROW " + str(r + 1) + "----")
        for c in range(n):
            sqArr[r][c] = int(input("Enter value: "))
    
# This procedure "pretty" prints a 2D square array of size n
def printSquare(n, sqArr):
    for r in range(n):
        for c in range(n):
            print(sqArr[r][c], end="\t")
        print("\n")

# This procedure will return true if every row of sqArr has a sum of mNum
def checkRow(n, sqArr, mNum):
    for r in range(len(sqArr)):
        sum = 0
        for c in range(len(sqArr[r])):
            sum += sqArr[r][c]

        if sum != mNum:
            return False

    return True

# This procedure will return true if every column of sqArr has a sum of mNum
def checkCol(n, sqArr, mNum):
    for r in range(len(sqArr)):
        sum = 0
        for c in range(len(sqArr[r])):
            sum += sqArr[c][r]

        if sum != mNum:
            return False

    return True

# This procedure will return true if the main diagonal has a sum of mNum
def checkDiag1(n, sqArr, mNum):
    sum = 0
    for i in range(len(sqArr)):
        sum += sqArr[i][i]

    if sum == mNum:
        return True
    else:
        return False

# This procedure will return true if the other diagonal has a sum of mNum
def checkDiag2(n, sqArr, mNum):
    sum = 0
    for i in range(len(sqArr)):
        sum += sqArr[i][(len(sqArr) - 1) - i]

    if sum == mNum:
        return True
    else:
        return False

# This procedure will return true if every element of sqArr is unique
def checkUnique(n, sqArr):
    expandedSqArr = []
    for r in range(len(sqArr)):
        for c in range(len(sqArr[r])):
            expandedSqArr.append(sqArr[r][c])

    for i in range(1, (3 ** 2) + 1):
        if i not in expandedSqArr:
            return False

    return True

# This procedure will return true if all the prodecures above return true
def checkSquare(size, square):
    """
    Returns True if inputed square is magic, and False if not.
    """
    magicNum = size * (size ** 2 + 1) / 2
    if (
        checkRow(size, square, magicNum) and  \
        checkCol(size, square, magicNum) and  \
        checkDiag1(size, square, magicNum) and  \
        checkDiag2(size, square, magicNum) and \
        checkUnique(size, square)
       ):
       return True
    else:
       return False

# Main program
s = int(input("Enter square side length: "))
sq = [[0 for x in range(s)] for y in range(s)]
fillSquare(s, sq)

printSquare(s, sq)
print(checkSquare(s, sq))
   

