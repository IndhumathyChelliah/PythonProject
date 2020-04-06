import unittest
import calc

class TestCalc(unittest.TestCase):
  def test_add(self):
    result=calc.add(10,5)
    self.assertEqual(result,15)
    self.assertEqual(calc.add(-1,-1),-2)


  def test_sub(self):
    result=calc.sub(10,5)
    self.assertEqual(result,5)
    self.assertEqual(calc.sub(-1,-1),0)

 
  def test_mul(self):
    result=calc.mul(10,5)
    self.assertEqual(result,50)
    self.assertEqual(calc.mul(-1,-1),1)

  def test_divide(self):
    result=calc.divide(10,5)
    self.assertEqual(result,2)
    self.assertEqual(calc.divide(-1,-1),1)
    self.assertRaises(ValueError,calc.divide,5,0)
    with self.assertRaises(ValueError):
    	calc.divide(5,0)

if __name__ =='__main__':
  unittest.main()
