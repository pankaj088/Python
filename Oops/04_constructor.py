
class Sinor:

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print("he is a good man ")

    def printDetails(self):
        print(f"His name is {self.name}")
        print(f"He is {self.age}")
        print(f"He is from {self.city}")


Bhayia = Sinor("shiv", 25, "bokaro")
Bhayia.printDetails()
# # __init__ khud call kar deta hai oo  object nhi banta hai


class MessRoutin:

    def __init__(self, monday, tuesday, wednesday):
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        print(" Time pass")

    def printlist(self):

        print(f"Moday ko -{self.monday}")
        print(f"Tuesday ko -{self.tuesday}")
        print(f"Wednesday ko -{self.wednesday}")


Khana = MessRoutin(" anda chwal", " machli chwal", " chicken chwal")
Khana.printlist()
