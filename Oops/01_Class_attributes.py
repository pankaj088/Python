'''
Noun     -->       class    -->    employee
adjective-->   Attributes   -->   name, age,salery
verb     -->    methods    -->  getsalery(), incriment()

'''


class Employee:
    company = "google"


nitish = Employee()
print(nitish.company)

# change company name
Employee.company = "Youtube"
print(nitish.company)
