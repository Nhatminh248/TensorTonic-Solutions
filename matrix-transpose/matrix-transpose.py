import numpy as np
def matrix_transpose(A):
    A = np.array(A)
    rows, cols = A.shape
    transpose = np.zeros((cols, rows))
    for row in range(rows):
        for col in range(cols):
            transpose[col][row] = A[row][col]  # ✅
    return transpose