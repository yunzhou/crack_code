import numpy as np

N=8
board = np.zeros((N, N))
board[0,2]=1
board[1,2]=1
board[6,3]=1
board[4,4]=1
board[7,0]=1
print(board)
current_path = []

def is_free(x, y):
    return board[x, y] == 0


def get_path(x, y):
    p = (x, y)
    current_path.append(p)
    if (x == 0 and y == 0):
        return True
    success = False
    if (x >= 1 and is_free(x - 1, y)):
        success = get_path(x - 1, y)  # go right
    if (not success and y >= 1 and is_free(x, y - 1)):
        success = get_path(x, y - 1)  # go right
    if (not success):
        current_path.remove(p)
    return  success

if __name__ == '__main__':
    get_path(N-1, N-1)
    print(current_path)
