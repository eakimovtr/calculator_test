import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculator(42, 69)
    
    def test_init_raises_error_when_nonnumber_passed(self):
        with self.assertRaises(TypeError):
            Calculator("hello", "world")
        with self.assertRaises(TypeError):
            Calculator("hello", 42)
        with self.assertRaises(TypeError):
            Calculator(42, "world")
        with self.assertRaises(TypeError):
            Calculator("hello", 3.14)
        with self.assertRaises(TypeError):
            Calculator(3.14, "world")
    
    def test_add(self):
        self.assertEquals(111, self.calc.add())
    
    def test_sub(self):
        self.assertEquals(-27, self.calc.sub())
        
    def test_mul(self):
        self.assertEquals(2898, self.calc.mul())
        
    def test_div(self):
        self.assertAlmostEquals(0.60869, self.calc.div(), 3)
        
    def test_max(self):
        self.assertEquals(69, self.calc.max())
        
    def test_min(self):
        self.assertEquals(42, self.calc.min())
        
    def test_percent(self):
        self.assertAlmostEquals(28.98, self.calc.percent(), 3)
        
    def test_power(self):
        self.assertEquals(42 ** 69, self.calc.power())
        
        
if __name__ == '__main__':
    unittest.main()