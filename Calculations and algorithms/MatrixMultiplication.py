import random

a = [[random.randrange(10) for i in range(0, 8)] for j in range(0, 8)]
b = [[random.randrange(10) for i in range(0, 8)] for j in range(0, 8)]

matrix = [[sum([ a[j][p]*b[p][i] for p in range(0,8)]) for i in range(0, 8)] for j in range(0, 8)]

print(a)
print(b)
print(matrix)