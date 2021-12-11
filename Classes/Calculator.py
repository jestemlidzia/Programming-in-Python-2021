import math
import re

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

class Calculator:
    def __init__(self, text):
        temp = False
        if text[1] == '-':
            temp = True
        
        text = text.replace('i', '')
        text = text.replace('(', '')
        text = text.replace(')', '')
        numbers = re.split('; |, |\+|\-|\*|/',text)

        i = 0
        for x in numbers:
            if x == '':
                del numbers[i]
            i=i+1

        operators = re.split('[0-9]+', text, flags=re.IGNORECASE)

        i = 0
        for x in operators:
            if x == '':
                del operators[i]
            i=i+1

        j = 0
        for x in operators:
            if len(x) == 2:
                operators.insert(j+1, operators[j][1])
                operators[j] = operators[j][0]
            j=j+1

        #print(numbers)
        #print(operators)

        sign = {
            "+": 1,
            "-": -1
        }
        if len(operators) == 3:
            self.operation = operators[1]
            del operators[1]
            self.right_val = ComplexNumber(int(numbers[0]), sign[operators[0]]*int(numbers[1]))
            self.left_val = ComplexNumber(int(numbers[2]), sign[operators[1]]*int(numbers[3]))
        elif len(operators) == 4:
            if temp:
                self.operation = operators[2]
                del operators[2]
                self.right_val = ComplexNumber(-1 * int(numbers[0]), sign[operators[1]]*int(numbers[1]))
                self.left_val = ComplexNumber(int(numbers[2]), sign[operators[2]]*int(numbers[3]))
            else:
                self.operation = operators[1]
                del operators[1]
                self.right_val = ComplexNumber(int(numbers[0]), sign[operators[0]]*int(numbers[1]))
                self.left_val = ComplexNumber(-1*int(numbers[2]), sign[operators[2]]*int(numbers[3]))
        elif len(operators) == 5:
            self.operation= operators[2]
            del operators[2]
            self.right_val = ComplexNumber(-1*int(numbers[0]), sign[operators[1]]*int(numbers[1]))
            self.left_val = ComplexNumber(-1*int(numbers[2]), sign[operators[3]]*int(numbers[3]))

        #print(self.operation)
        #print(self.right_val)
        #print(self.left_val)
    
    def __call__(self):
        if(self.operation == "+"):
            return self.right_val + self.left_val
        elif(self.operation == "-"):
            return self.right_val - self.left_val
        elif(self.operation == "*"):
            return self.right_val * self.left_val
        elif(self.operation == "/"):
            return self.right_val / self.left_val



i = ComplexNumber(2, 1)
k = ComplexNumber(2, 2)
#print(abs(i+k))

a = Calculator('(-5+3i)*(-4-5i)')
b = Calculator('(-4-6i)+(4+6i)')
c = Calculator('(8-12i)-(-4+6i)')
d = Calculator('(4-6i)/(4+6i)')

print(a())
print(b())
print(c())
print(d())