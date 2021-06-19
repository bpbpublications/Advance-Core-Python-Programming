#6.4 How to debug a program?
class Student:
    def __init__(self, name, email, department, age):
        self.name = name
        self.email = email
        self.department = department
        self.age = age

    def print_student(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Department : ",self.department)
        print("Age : ",self.age)


s1 = Student("Alex","alex@company_name.com","Electronics",18)
s1.print_stdent()

########
class Student:
    def __init__(self, name, email, department, age):
        self.name = name
        self.email = email
        self.department = department
        self.age = age

    def print_student(self):
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Department : ",self.department)
        print("Age : ",self.age)


s1 = Student("Alex","alex@company_name.com","Electronics",18)
s1.print_student()
