import math

class complex_numbers():
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b
    def __add__(self, self1):
        return complex_numbers(self.a + self1.a, self.b + self1.b)
    def __sub__(self, self1):
        return complex_numbers(self.a - self1.a, self.b - self1.b)
    def __mul__(self, self1):
        return complex_numbers(self.a * self1.a - (self.b * self1.b), self.a * self1.b + (self.b * self1.a))
    def __truediv__(self, self1):
        s1 = (self.a * self1.a + self.b * self1.b) / (self1.a ** 2 + self1.b ** 2)
        s2 = (self1.a * self.b - self1.b * self.a) / (self1.a ** 2 + self1.b ** 2)
        return complex_numbers(s1, s2)
    def __str__(self):
        if self.b < 0:
            return str(self.a) + '' + str(self.b) + 'i'
        return str(self.a) + '+' + str(self.b) + 'i'
    @staticmethod
    def mod(self):
        return ((self.a ** 2) + (self.b ** 2)) ** 0.5
    def __pow__(self, n):
        z = self
        #print(z)
        c = z
        while n - 1 != 0:
            c = c * z
            n = n - 1
        return c
    @staticmethod
    def arg(self):
        r = (self.a ** 2 + self.b ** 2) ** 0.5
        return math.asin(self.b / r)
        
    
        

x = complex_numbers(1, -2)
y = x + x
z = x - x
s1 = complex_numbers(1, -1)
s2 = complex_numbers(3, 6)
q1 = complex_numbers(2, 3)
q2 = complex_numbers(5, -7)
print(x)
print(y)
print(z)
print(s1 * s2)
q = q1 / q2
print(q)
z = complex_numbers(1, 1)
print(z ** 3)
print(complex_numbers.arg(z))
