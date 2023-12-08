import numpy as np
from itertools import product
import time

def checkKnight(x,y,n):
    global sudoku
    moves = list(product([x-1, x+1], [y-2, y+2])) + list(product([x-2, x+2], [y-1, y+1]))
    moves = [(x, y) for x, y in moves if x >= 0 and y >= 0 and x < 9 and y < 9]
    for i in moves:
        if sudoku[i[0]][i[1]] == n:
            return True
    return False

def checkKings(x,y,n):
    global sudoku
    moves = list(product([x-1, x+1],[y-1, y+1]))
    moves = [(x, y) for x, y in moves if x >= 0 and y >= 0 and x < 9 and y < 9]
    for i in moves:
        if sudoku[i[0]][i[1]] == n:
            return True
    return False

def trial(x,y,n):
    global sudoku
    global knightmove
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
    if kingsmove == 1:
        if checkKings(x,y,n):
            return False
    if knightsmove == 1:
        if checkKnight(x,y,n):
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

    knightsmove = 0 #Toggle for Knight's move constraint
    kingsmove = 1 #Toggle for Knig's move constraint
    counter = 0
    sudoku = [[3,0,7,0,5,0,0,0,6],
              [0,0,4,0,1,0,0,3,0],
              [0,0,0,0,0,0,2,0,0],
              [0,4,0,0,0,0,0,0,0],
              [0,0,0,7,0,0,0,4,0],
              [0,0,0,0,0,2,0,5,9],
              [0,5,0,0,0,8,0,0,0],
              [8,9,0,0,0,0,0,0,3],
              [0,0,1,0,6,0,5,2,0]]
    solve()
