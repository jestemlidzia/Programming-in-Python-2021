import math

a = int(input("a value: "))
b = int(input("b value: "))
c = int(input("c value: "))

delta = b*b - 4*a*c

if delta > 0:
    sqrDelta = math.sqrt(delta)
    x1 = (- b - sqrDelta)/(2*a)
    x2 = (- b + sqrDelta)/(2*a)
    print("Equation has got two roots: ", x1, " and ", x2)
elif delta == 0:
    x0 = (-b)/(2*a)
    print("Equation has got only one root: ", x0)
elif delta < 0:
    print("There's no roots")
