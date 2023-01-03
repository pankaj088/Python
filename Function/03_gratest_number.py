
def maxium_number(num1, num2, num3):
    if (num1 > num2):
        if (num1 > num3):
            return num1
        else:
            return num3
    if (num2 > num3):
        return num2
    else:
        return num3


print(maxium_number(3, 9, 6))
