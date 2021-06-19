def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y==0):
        str1 = "invalid denominator"
        return str1
    else:
        return x/y
##############################33
import arith_funcs
import unittest

class TestArithFuncs(unittest.TestCase):
#Define Testing Methods

    def test_add(self):
        self.assertEqual(30,arith_funcs.add(10,20))

    def test_subtract(self):
        self.assertEqual(-10,arith_funcs.subtract(10,20))

    def test_multiply(self):
        self.assertEqual(200,arith_funcs.multiply(10,20))

    def test_divide(self):
        self.assertEqual("zero not allowed as denominator",arith_funcs.divide(10,0))
        self.assertEqual(2,arith_funcs.divide(10,5))

unittest.main()
#################
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if(y==0):

#Change of code:
 str1 = "zero not allowed as denominator"
        return str1
    else:
        return x/y
