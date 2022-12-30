MyDict = {
    "Name": "pankaj kumar",
    "Roll": 54,
    "Section": "B",
}

print(MyDict["Name"])
print(MyDict['Roll'])
print(MyDict["Section"])
print(type(MyDict))

# prints the keys of dictionary
print(MyDict.keys())

# print the values of dictionary
print(MyDict.values())

# print the items of dictionary
print(MyDict.items())


# pratice sets
# Questions-1
Dictionary = {
    "aam": "mango",
    "kela": "banana",
    "papita": "papya",
}
a = Dictionary.keys()
print(type(a))
a = input("Enter the hindi word\n : ")
print(Dictionary[a])
