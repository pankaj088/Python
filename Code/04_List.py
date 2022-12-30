L = ["pankaj", "kumar", "54", "2019"]
L[0] = "Birju"
print(L)

# List slicing- yai 0 to 2 se pahle tak print kar dega
print(L[0:2])

# list sorting
L1 = [2, 8, 9, 1, 0, 12]
L1.sort()
print(L1)

# reversed
L1.reverse()
print(L1)

# append - yani ki last mai 3 add kar dega
L1.append(3)
print(L1)

# insert(2,80) - yani ki 80 print hoga index 2 pai
L1.insert(2, 80)
print(L1)

# pop(2) - yani ki index 2 pai jo element ayiga usko delate kar dega
L1.pop(2)
print(L1)

# remove(0) - yani ki yai 0 ko remove kar dega
L1.remove(0)
print(L1)

# partice set qoustion'
# question -1
f1 = input("enter first fruit : ")
f2 = input("enter second fruit : ")
f3 = input("enter third fruit : ")
f4 = input("enter fourth fruit : ")
f5 = input("enter fifth fruit : ")

FruitList = [f1, f2, f3, f4, f5]
print(FruitList)

# question-4

S = [5, 8, 45, 60]
print(S[0] + S[1] + S[2] + S[3])
print(sum(S))
