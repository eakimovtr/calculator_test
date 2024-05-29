import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
        
    def test_init_throws_when_nonint_passed(self):
        with self.assertRaises(TypeError):
            Fraction(3.14, 42)
        with self.assertRaises(TypeError):
            Fraction(42, 2.71828)
        
    def test_reducing(self):
        fraction = Fraction(18,20)
        
        self.assertEqual(9, fraction.numerator)
        self.assertEqual(10, fraction.denominator)
        
    def test_inversing_signs_when_both_values_are_negative(self):
        fraction = Fraction(-1,-2)
        
        self.assertEqual(1, fraction.numerator)
        self.assertEqual(2, fraction.denominator)
        
    def test_sum(self):
        fraction1 = Fraction(2,7)
        fraction2 = Fraction(3,9)
        
        res = fraction1 + fraction2
        
        self.assertEqual(Fraction(13,21), res)
        
    def test_subtraction(self):
        fraction1 = Fraction(6,8)
        fraction2 = Fraction(1,4)
        
        res = fraction1 - fraction2
        
        self.assertEqual(Fraction(1,2), res)
        
    def test_multiply_raises_error_when_nonnumber_passed(self):
        fraction = Fraction(2,3)
        factor = "string"
        with self.assertRaises(TypeError):
            fraction * factor
    
    def test_multiply_on_int(self):
        fraction = Fraction(2,3)
        factor = 3
        
        res = fraction * factor
        
        self.assertEqual(Fraction(6,3), res)
        
    def test_multiply_on_fraction(self):
        fraction = Fraction(2,3)
        factor = Fraction(4,5)
        
        res = fraction * factor
        
        self.assertEqual(Fraction(8,15), res)
    
    def test_division_on_int(self):
        fraction = Fraction(14,21)
        factor = 7
        
        res = fraction / factor
        
        self.assertEqual(Fraction(2,21), res)
        
    def test_division_on_fraction(self):
        fraction = Fraction(7,9)
        factor = Fraction(8,11)
        
        res = fraction / factor
        
        self.assertEqual(Fraction(77,72), res)
    
        
        
if __name__ == '__main__':
    unittest.main()