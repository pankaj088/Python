

Fruits = ["Mango", "Banana", "orage", "watermalon"]

for item in Fruits:
    print(item)

# Range function(1,9)- yaha 1 to 8 tak print hoga
for j in range(9):
    print(j)
    print('\n')

# Step down(,2)- mai 2 ko chorkar print kariga
for k in range(1, 9, 2):
    print(k)
else:
    print("Done")
    print("\n")


# break statment
for l in range(1, 9,):
    print(l)
    if l == 5:
        break
    # break kai bad else print nhi hoga
else:
    print("Done")


# Countinue statment- mai (m==5) yani ki 5 ko chorkar 0 to 9 tak print kar dega
for m in range(10):
    if m == 5:
        continue
    print(m)


# Pass statment - is a null statement
for n in range(6):

    if n < 6:
        pass
       
    # yai pass kar dega agar kuch nhi bhi likhege to bhi error nhi dega
