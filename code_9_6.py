# Given a matrix in which each row and each column is sorted, write a method to find an element in it.
def find_elem_in_mat(mat, x):
    M = len(mat)  # rows
    N = len(mat[0])  # cols
    row = 0
    col = N - 1
    while row < M and col >= 0:
        if mat[row][col] == x:
            return True
        elif x > mat[row][col]:
            row += 1
        elif x < mat[row][col]:
            col -= 1
    return False
