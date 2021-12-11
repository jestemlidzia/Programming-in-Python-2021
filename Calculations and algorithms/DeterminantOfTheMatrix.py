import random as r

def helper(matrix, i, j):
    return [row[: j] + row[j+1:] for row in (matrix[: i] + matrix[i+1:])]
 
def Determinant(matrix):
    if(len(matrix) == 2):
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    result = 0
 
    for column in range(len(matrix)):
        temp = Determinant(helper(matrix, 0, column))
        result = result + (((-1) ** (column)) * matrix[0][column] * temp)

    return result
    
size = r.randrange(8)
m = [[r.randrange(11) for i in range(0, size)] for j in range(0, size)]

print('Determinant: ', Determinant(m))