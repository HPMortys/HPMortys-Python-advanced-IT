class Complex_num():
    """Complex calculator"""
    def __init__(self,a,b):
        self.a = a
        self.b =b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return f'{a} + {b}i'

    def __sub__(self, other):
        a = self.a - other.a
        b = self.b - other.b
        return f'{a} + {b}i'

    def __mul__(self, other):
        a = self.a * other.a - self.b * other.b
        b = self.a * other.b + self.b * other.a
        return f'{a} + {b}i'


compl = Complex_num(4,1)
compl1 = Complex_num(2,1)



print(compl * compl1)



