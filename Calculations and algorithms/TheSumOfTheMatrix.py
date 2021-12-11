import random

matrix1 = [[random.randrange(100) for i in range(1, 129)] for j in range(1, 129)]
matrix2= [[random.randrange(100) for i in range(1, 129)] for j in range(1, 129)]

matrixSum = [[matrix1[j][i]+matrix2[j][i] for i in range(0, 128)] for j in range(0, 128)]
print(matrixSum[0][0])
print(matrix1[0][0])
print(matrix2[0][0])