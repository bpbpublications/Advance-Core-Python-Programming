#1
class classLevel:
    def class1(self,string_a):
        print(string_a)

    def class2(self):
        print('There are 15 students in this class')

cl = classLevel("Hello")
cl.class1()
cl.class2()
#######################################

class Foo:
    @staticmethod
    def bar():
        print('Static method bar()')

    @staticmethod
    def stat():
        print("Static method stat()")

    def class1(self,string_a):
        print(string_a)

# Calling static method  bar()
Foo.bar()

# Calling static method  stat()
Foo.stat()

#calling bounded method class1()
f = Foo()
f.class1('bounded method')


######################################33
#2
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

b1 = Bank('customer1','10000')
b2 = Bank('friend','10000')

#print values of b1 and b2
print(b1)
print(b2)

#print values of b1 and b2
b1+b2
#################################3
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        str1 = 'name: '+self.name+' balance:  '+self.balance+'.'
        return str1

    def __add__(self, other):
        balance = int(self.balance) + int(other.balance)
        return balance

b1 = Bank('customer1','10000')
b2 = Bank('friend','10000')

#print values of b1 and b2
print(b1)
print(b2)

#print values of b1 and b2
print(b1 + b2)
