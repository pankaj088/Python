
# self -> ak paramiter hai jo kisi object pai kue function call karne pai (self) khud automatic pass hota hai
class student:
    def getroll_num(self):
        print(" roll number is " + str(5554))

# @staticmethod - me self nhi likhte hai kuki yai decorate function hai
    @staticmethod
    def greet():
        print(" Good morning")


rishav = student()
rishav.getroll_num()
rishav.greet()
