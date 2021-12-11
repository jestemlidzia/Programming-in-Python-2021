import math

class ComplexNumber:
    def __init__(self, real=0.0, imag=0.0):
        self.r = real
        self.i = imag

    def __str__(self):
        return '(%s, %si)' % (self.r, self.i)

    def __add__(self, a):
        return ComplexNumber(self.r + a.r, self.i + a.i)

    def __sub__(self, a):
        return ComplexNumber(self.r - a.r, self.i - a.i)
    
    def __mul__(self, a):
        return ComplexNumber(self.r * a.r - self.i * a.i, self.i * a.r + self.r * a.r)
    
    def __truediv__(self, a):
        r = (a.r**2 + a.i**2)
        return ComplexNumber((self.r * a.r - self.i * a.i) / r, (self.i * a.r + self.r * a.i) / r)

    def __abs__(self):  
        temp = math.sqrt(self.r**2 + self.i**2)
        return ComplexNumber(temp)

i = ComplexNumber(2, 1)
k = ComplexNumber(2, 2)
print(abs(i+k))
