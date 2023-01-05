
class C_2dvector:

    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i +  {self.jcap}j"


class C_3dvector:

    def __init__(self, i, j, k):
        # super().__init__(i, j)
        self.icap = i
        self.jcap = j
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"


V2d = C_2dvector(2, 3)
V3d = C_3dvector(1, 3, 5)
print(V2d)
print(V3d)
