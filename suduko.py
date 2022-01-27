# solversudoku(puzzle)
# find_next_empty(puzzle)
# guess_validation(puzzle,row,col,guess)
# main



def find_next_empty(puzzle):
    for i in range(0,9):
        for j in range(0,9):
            if(puzzle[i][j]==-1):
                return i,j
    return None,None

def guess_validation(puzzle,row,col,guess):
    row_values =  puzzle[row]
    for i in range(0,9):
        if(guess==row_values[i]):
            return False

    col_values =  []  
    for i in range(0,9):
        col_values.append(puzzle[i][col])
    for j in range(0,9):
        if(guess==col_values[j]):
            return False

    row1=(row//3)*3
    col1=(col//3)*3
    for i in range(row1,row1+3):
        for j in range(col1,col1+3):
            if(guess==puzzle[i][j]):
                return False
    return True



def solversudoku(puzzle):
    row,col=find_next_empty(puzzle)
    if (row==None):
        return True
    for guess in range (1,10):
        guess1 = guess_validation(puzzle,row,col,guess)
        if (guess1==True):
            puzzle[row][col]=guess
            solversudoku(puzzle)
        puzzle[row][col]=-1
    return False


a=[

    [6,9,1,-1,-1,-1,-1,-1,5],
    [-1,-1,-1,3,-1,-1,-1,8,1],
    [2,3,8,1,-1,-1,4,6,-1],
    []
]