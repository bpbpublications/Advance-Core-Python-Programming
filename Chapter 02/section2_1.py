### All code boxes of section 2.1 Classes and Objects
class Employee:
    def __init__(self, name, email, department, age, salary):
        self.name = name
        self.email = email
        self.department = department
        self.age = age
        self.salary = salary
#####

class Employee:
    def __init__(self, a, b, c, d, e):
        self.name = a
        self.email = b
        self.department = c
        self.age = d
        self.salary = e

##########

class Employee:
    def __init__(self, name, email, department, age, salary):
        self.name = name
        self.email = email
        self.department = department
        self.age = age
        self.salary = salary

e1 = Employee("Alex","alex@company_name.com","Finance",42,500000)


###########
def print_employee(self):
    print("Name : ",self.name)
    print("Email : ",self.email)
    print("Department : ",self.department)
    print("Age : ",self.age)
    print("Salary : ",self.salary)

##########

e1.print_employee()

#############
class Employee:
    def __init__(self, name, email, department, age, salary):
        self.name = name
        self.email = email
        self.department = department
        self.age = age
        self.salary = salary

    def print_employee(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Department : ",self.department)
        print("Age : ",self.age)
        print("Salary : ",self.salary)

e1 = Employee("Alex","alex@company_name.com","Finance",42,500000)
e1.print_employee()

####################

class Employee:
    def __init__(self, name, email, department, age, salary):
        self.name = name
        self.email = email
        self.department = department
        self.age = age
        self.salary = salary

    def print_employee(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Department : ",self.department)
        print("Age : ",self.age)
        print("Salary : ",self.salary)

e1 = Employee("Alex","alex@company_name.com","Finance",42,500000)
e1.print_employee()

e2 = Employee("Evan","evan@company_name.com","HR",34,300000)
e2.print_employee()

e3 = Employee("Maria","maria@company_name.com","HR",30,350000)
e3.print_employee()

e4 = Employee("Pradeep","pradeep@company_name.com","IT",28,700000)
e4.print_employee()

e5 = Employee("Simon","simon@company_name.com","Finance",40,500000)
e5.print_employee()

e6 = Employee("Venkatesh","venkatesh@company_name.com","Sales",25,200000)
e6.print_employee()
