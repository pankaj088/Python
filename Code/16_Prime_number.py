
Num = int(input(" Enter the number : "))
fl =1
for p in range(2, Num):
    if (Num % p == 0):
        print("Number is not prime")
        fl=0
        break

if(fl ==1):
    print("Number is prime")