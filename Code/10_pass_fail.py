S1 = int(input(" Enter first subect marks : "))
S2 = int(input(" Enter second subect marks : "))
S3 = int(input(" Enter third subect marks : "))


if (S1 < 30 and S2 < 30 and S3 < 30):
    print(" you are fail in one subject")
elif (S1+S2+S3)/3 < 40:
    print(" you are fail bcz total marks less than 40")
else:
    print("you have passed sucessfully examination")
