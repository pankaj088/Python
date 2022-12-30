
a = 10
if (a > 15):
    print(" a is grater than 15 ")

elif (a > 25):
    print(" a is grater than 25")

else:
    print(" a is not garter than 15 and 25 ")


# # Quick quiz
Age = int(input(" Enter your age : "))
if (Age > 18):
    print("yes you can enjoy")
else:
    print("no you can't enjoy ")


# # and operator
Age = int(input(" Enter your age : "))
if (Age > 18 and Age < 50):
    print("you can drive")

else:
    print("you can't drive")

# # or operator
Age = int(input(" Enter your age : "))
if (Age < 18 or Age > 50):
    print("you can drive")

else:
    print("you can't drive")


# is operator
a = None
if (a is None):
    print("yes")
else:
    print("No")


# in operator
b = [3, 6, 8]
print(81 in b)
# agar list mai rahiga to true print kariga nhi to false
