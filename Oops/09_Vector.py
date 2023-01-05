
class Vector:

    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "

    # For finding the length of vector
    def __len__(self):
        return len(self.vec)


V1 = Vector([1, 4, 8])
V2 = Vector([3, 6, 9])
print(V1)
print(V2)
print(len(V1))
