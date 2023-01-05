
# single inheritance  - mai ak Base class or ak derived class hoga
class Father:
    Fname = " Raja Dashrat"

    def __init__(self):
        print("This is Base class ")

    def getresult(self):
        print(f" {self.Fname}")


class Son(Father):
    Sname = " Shree Ram"

    def __init__(self):
        print("This is derived class ")

    def getresult(self):
        print(f" {self.Sname}")


F = Father()
F.getresult()

S = Son()
S.getresult()


# multiple inheritance - bahut sare : Base class(Father , Son) : kai ak hi :  Derived class(Grandson): honge

class Father:
    Fname = " Raja Dashrat"

    def __init__(self):
        print("This is Base class ")

    def getresult(self):
        print(f" {self.Fname}")


class Son():
    Sname = " Shree Ram"

    def __init__(self):
        print("This is Base class ")

    def getresult(self):
        print(f" {self.Sname}")


class Grandson(Father, Son):
    Gname = "Luv , kush "

    def __init__(self):
        print("This is derived class")

    def showname(self):
        print(f" {self.Gname}")


F = Father()
F.getresult()

S = Son()
S.getresult()

G = Grandson()
G. showname()


# multilevel inheritance - mai ak : Base(Father): kai bahut sare : Derived class(S0n , grandson) : honge

class Father:
    Fname = " Raja Dashrat"

    def __init__(self):
        print("This is Base class ")

    def getresult(self):
        print(f" {self.Fname}")


class Son(Father):
    Sname = " Shree Ram"

    def __init__(self):
        print("This is Derived class ")

    def getresult(self):
        print(f" {self.Sname}")


class Grandson(Son):
    Gname = "Luv , kush "

    def __init__(self):
        print("This is derived class")

    def showname(self):
        print(f" {self.Gname}")


F = Father()
F.getresult()

S = Son()
S.getresult()

G = Grandson()
G. showname()
