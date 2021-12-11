a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

x = sum([a[i]*b[i] for i in range(0, 4)])
print("Scalar product: ", x)