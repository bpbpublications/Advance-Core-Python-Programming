class Students:
    student_id = 50

    # This is a special function that Python calls when you create new instance of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Students.student_id = Students.student_id + 1
        print('Student Created')

    # This method keeps a count of total number of students
    def Total_no_of_students(self):
        print("Total Number of students in the school are : "+str(Students.student_id))


    def __del__(self):
        print('object {} life cycle is over. '.format(self.name))

# create an object stu1
stu1 = Students('Paris', 12)
stu1.Total_no_of_students()

# destroy object stu1
del stu1

#Checking if the object still exists
stu1.Total_no_of_students()
