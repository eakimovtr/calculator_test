class Calculator:
    def __init__(self, term1, term2):
        if (type(term1) != int and type(term1) != float) or (type(term2) != int and type(term2) != float):
            raise TypeError("Can only operate numbers")
        self.term1 = term1
        self.term2 = term2
        
    def add(self):
        return self.term1 + self.term2
    
    def sub(self):
        return self.term1 - self.term2
    
    def mul(self):
        return self.term1 * self.term2
    
    def div(self):
        return self.term1 / self.term2
    
    def max(self):
        return max(self.term1, self.term2)
    
    def min(self):
        return min(self.term1, self.term2)
    
    def percent(self):
        return self.term1 * self.term2 / 100
    
    def power(self):
        return self.term1 ** self.term2