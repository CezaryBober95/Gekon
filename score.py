import numpy as np

#todo: array with float values

file = open("Raport_Reks.txt", "rt")
contents=file.read()
file.close()
print(contents)
def create_board():
    board=np.zeros((8,8))
    return board

def add_score(board,row,col):
    board[row][col]+=1
    return board


#board_real=create_board()
#gen=score_gen(board_real)
#print(board_real)


