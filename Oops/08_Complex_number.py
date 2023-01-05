
class Complex:

    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, c):
        return complex(self.real + c.real, self.imaginary + c.imaginary)

    def __str__(self):
        return f"{self.real}r + {self.imaginary}i"


C1 = complex(4, 8)
C2 = complex(3, 9)
print(C1+C2)
