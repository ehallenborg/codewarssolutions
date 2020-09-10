import numpy as np

def determinant(matrix):    
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] -  matrix[0][1] * matrix[1][0]
    else:
        return int(determinant_recursive(matrix))
    
def determinant_recursive(A, total=0):
    indices = list(range(len(A)))
    
    # when at 2x2 submatrices recursive calls end
    if len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val
        
    for fc in indices:
    # find the submatrix
        As = A.copy() # make a copy
        As = As[1:] # remove the first row
        height = len(As) # D) 
        
        for i in range(height): 
        # for each remaining row of submatrix remove the focus column elements
            As[i] = As[i][0:fc] + As[i][fc+1:] 
            
        sign = (-1) ** (fc % 2) # F) 
        # pass submatrix recursively
        sub_det = determinant_recursive(As)
        # total all returns from recursion
        total += sign * A[0][fc] * sub_det 
        
    return total

    
def big_matrix(A):
    n = len(A)
    
    for fd in range(n): # fd stands for focus diagonal
        for i in range(fd + 1,n): # only use rows below fd row
            if A[fd][fd] is 0: # if diagonal is zero
                A[fd][fd] == 1.0e-10 # change to ~zero
            # cr stands for "current row"
            print(A[i][fd] / A[fd][fd])
            cr = A[i][fd] / A[fd][fd]
            # cr - crScaler * fdRow, one element at a time
            for j in range(n): 
                A[i][j] = A[i][j] - cr * A[fd][j]
            
    # Once A is in upper triangle form
    product = 1.0
    for i in range(n):
        product *= A[i][i] 
    
    return product
    