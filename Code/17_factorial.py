num = int(input("Enter number "))

factorial = 1
for i in range(1, num+1):
    factorial = factorial * i
    print(f" factorial number {num} is {factorial}")

# 5! = 5 x 4 x 3 x 2 x1 