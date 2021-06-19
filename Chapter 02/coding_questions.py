#1
class Kite:
    def fly(self):
        print('is meant to fly')
k = Kite()
k.fly()
###################
#2
class classLevel:
    def class1(self):
        print('There are 20 students in this class')
    def class2(self):
        print('There are 15 students in this class')
    def class3(self):
        print('There are 41 students in this class')
    def class4(self):
        print('There are 30 students in this class')

cl = classLevel()
cl.class3()
###################3
#3
class Twice_multiply:
    def __init__(self):
        self.calculate(500)

    def calculate(self, num):
        self.num = 2 * num;

class Thrice_multiply(Twice_multiply):
    def __init__(self):
        super().__init__()
        print("num from Thrice_multiply is", self.num)

    def calculate(self, num):
        self.num = 3 * num;

tm = Thrice_multiply()
##########################3
#4
class Twice_multiply:
    def __init__(self):
        self.calculate(500)

    def calculate(self, num):
        self.num = 2 * num;

class Thrice_multiply(Twice_multiply):
    def __init__(self):
        super().__init__()
        print("num from Thrice_multiply is", self.num)

    def calculate(self, num):
        self.num = 3 * num;

tm = Thrice_multiply()
##################################
#5
class Table:
    def features(x):
        print('This table has {} legs.' .format(x))
Table.features(4)
