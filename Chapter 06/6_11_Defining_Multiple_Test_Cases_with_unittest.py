#1.(I)	Defining multiple cases with unittest
import arith_funcs
import unittest

class TestArithFuncs(unittest.TestCase):
    #Define Testing Methods

    def test_add(self):
        vals = [(10,20),(20,78),(60,54),(13,25)]
        ans = [30,98,114,38]
        for i in range(len(vals)):
            self.assertEqual(ans[i],arith_funcs.add(vals[i][0],vals[i][1]))

    def test_subtract(self):
        self.assertEqual(-10,arith_funcs.subtract(10,20))

    def test_multiply(self):
        self.assertEqual(200,arith_funcs.multiply(10,20))

    def test_divide(self):
        self.assertEqual("zero not allowed as denominator",arith_funcs.divide(10,0))
        self.assertEqual(2,arith_funcs.divide(10,5))

unittest.main()
##############################
#1.(II)	Defining multiple test cases withpytest
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
#########################3
#test_arith_func.py
import arith_funcs

def test_add():
vals = [(10,20),(20,78),(60,54),(13,25)]
ans = [30,98,114,38]
    for i in range(len(vals)):
        assert arith_funcs.add(vals[i][0],vals[i][1]) == ans[i]

def test_subtract():
    assert arith_funcs.subtract(10,20) == -10

def test_multiply():
    assert arith_funcs.multiply(10,20) == 200

def test_divide():
    assert arith_funcs.divide(10,0) == "invalid denominator"
    assert arith_funcs.divide(10,5) == 2
    
