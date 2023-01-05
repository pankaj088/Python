
class employee:
    company = " paytm"
    # salery = 3000000 --> yai class attributes hai


raushan = employee()
print(raushan.company)
# yai instance attributes hai
raushan.salery = 30000
raushan.salery = 40000
print(raushan.salery)

employee.company = "Microsoft"
print(raushan.company)
print(raushan.salery)
