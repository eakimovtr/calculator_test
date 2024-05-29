import math

class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if (type(numerator) != int or type(denominator) != int):
            raise TypeError("Numerator and denominator must be integers")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()
        
    def reduce(self) -> None:
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if (self.numerator < 0 and self.denominator < 0):
            self.numerator = -self.numerator
            self.denominator = -self.denominator
    
    def __add__(self, other):
        res = Fraction((self.numerator * other.denominator + other.numerator * self.denominator), (self.denominator * other.denominator))
        return res
    
    def __sub__(self, other):
        res = Fraction((self.numerator * other.denominator - other.numerator * self.denominator), (self.denominator * other.denominator))
        return res
    
    def __mul__(self, other):
        if type(other) != Fraction and type(other) != int:
            raise(TypeError("Can only multiply on numbers"))
        if type(other) == int:
            other = Fraction(other, 1)
        res = Fraction((self.numerator * other.numerator), (self.denominator * other.denominator))
        return res
    
    def __truediv__(self, other):
        if type(other) != Fraction and type(other) != int:
            raise(TypeError("Can only divide on numbers"))
        if type(other) == int:
            other = Fraction(other, 1)
        res = self * Fraction(other.denominator, other.numerator)
        return res
    
    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator
    
    def __repr__(self) -> str:
        return f"{self.numerator}/{self.denominator}"