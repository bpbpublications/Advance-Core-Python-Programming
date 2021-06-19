import arith_funcs
import unittest

class TestArithFuncs(unittest.TestCase):
    #Define Testing Methods

    def test_add(self):
        vals = [(10,20),(20,78),(60,54),(13,25)]
        ans = [30,98,114,38]
        for i in range(len(vals)):
            self.assertEqual(ans[i],arith_funcs.add(vals[i][0],vals[i][1],))

    def test_subtract(self):
        self.assertEqual(-10,arith_funcs.subtract(10,20))

    def test_multiply(self):
        self.assertEqual(200,arith_funcs.multiply(10,20))

    def test_divide(self):
        self.assertEqual("zero not allowed as denominator",arith_funcs.divide(10,0))
        self.assertEqual(2,arith_funcs.divide(10,5))
  
unittest.main()
      
    
