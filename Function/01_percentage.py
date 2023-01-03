
Marks = [45, 50, 62, 80]
percentage = (sum(Marks)/400) * 100
print(percentage)
Marks2 = [30, 40, 50, 70, 80]
percentage1 = (sum(Marks2)/500) * 100
print(percentage1)

# Using function


def percent(marks):
    p = (sum(marks)/400)*100
    return p


Marks1 = [45, 50, 62, 80]
percentage1 = percent(Marks1)

Marks2 = [30, 40, 50, 70]
percentage2 = percent(Marks2)
print(percentage1, " ", percentage2)

# print message


def greet(name=" potlu"):
    print("happy new year 2023 " + name)


greet("LOLU")
greet()

# sum number


def NumberSum(a, b, c):
    return a+b+c


add = NumberSum(2, 4, 6)
print(add)
