
class number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num1):
        return self.num + num1.num

    def __mul__(self, num1):
        return self.num * num1.num


N1 = number(4)
N2 = number(6)
print(N1 + N2)
print(N1*N2)
