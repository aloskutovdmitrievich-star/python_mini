from math import *

class square_root():
    def __init__(self, a):
        self.a = a

    def square_root(self):
        res = sqrt(self.a)
        return res
    
class Calculator():
    """If you want add, then write:
    1. oCalculator = Calculator(144, 12)
    2. oCalculator = oCalculator.add()
    e t.c."""
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        result = self.a + self.b
        return result
    
    def sub(self):
        result = self.a - self.b
        return result
    
    def mul(self):
        result = self.a * self.b
        return result
    
    def div(self):
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            result = ZeroDivisionError()

        return result