
# for read
O = open('sample.txt1', 'r')
print(O.read())
# print(O.readline()) me ak line print kariag
O.close()

# for write
W = open('write.txt', 'w')
W.write("welcome in python course")
W.close()
