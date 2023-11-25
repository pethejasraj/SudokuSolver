import numpy as np
def trial(x,y,n):
    global sudoku
    for i in range(0,9): #Test row
        if sudoku [x][i] == n:
            return False
    for i in range(0,9): #Test column
        if sudoku [i][y] == n:
            return False
    x1 = (x//3)*3
    y1 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku[x1+i][y1+j] == n:
                return False
    return True

def solve():
    global sudoku
    for x in range(0,9):
        for y in range (0,9):
            if sudoku[x][y] == 0:
                for n in range(1,10):
                    if trial(x,y,n):
                        sudoku[x][y] = n
                        solve()
                        sudoku[x][y] = 0
                return
    print(np.matrix(sudoku))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    sudoku = [[1,2,3,0,0,7,6,0,5],
              [7,4,0,6,2,0,8,0,0],
              [6,8,0,0,0,0,0,0,0],
              [3,0,0,9,8,0,0,0,0],
              [2,0,0,4,5,6,0,3,0],
              [0,6,0,0,0,0,9,2,0],
              [0,0,0,3,0,0,0,0,0],
              [8,1,0,0,0,0,5,0,0],
              [0,3,0,0,6,0,7,8,9]]

    solve()

 #   solve(sudoku,0,0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
