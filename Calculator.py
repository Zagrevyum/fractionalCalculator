#class to resolve all the fraction operations
from Fraction import Fraction
# the class  takes 2 fractions objects and returns as a result a fraction object

class Calculator:
    def __init__(self, fraction_a: Fraction, fraction_b: Fraction):
        self.fraction_a = fraction_a
        self.fraction_b = fraction_b
        self.result = Fraction("")

##resolve fraction multiplication
    def multiplication(self) -> Fraction:
        numerator = self.fraction_a.numerator * self.fraction_b.numerator
        denominator = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(numerator, denominator)
        return self.result

##resolve division operation
    def division(self) -> Fraction:
        numerator = self.fraction_a.numerator * self.fraction_b.denominator
        denominator = self.fraction_a.denominator * self.fraction_b.numerator
        self.result.initialize_with_num_den(numerator, denominator)
        return self.result

##resolve sum operation
    def addition(self) -> Fraction:
        if self.fraction_a.denominator == self.fraction_b.denominator:
            numerator = self.fraction_a.numerator + self.fraction_b.numerator
            self.result.initialize_with_num_den(numerator, self.fraction_a.denominator)
            return self.result
        numerator = (self.fraction_a.numerator * self.fraction_b.denominator) + (self.fraction_a.denominator * self.fraction_b.numerator)
        den = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(numerator, den)
        return self.result

#resolve rest operation
    def subtraction(self) -> Fraction:
        if self.fraction_a.denominator == self.fraction_b.denominator:
            numerator = self.fraction_a.numerator - self.fraction_b.numerator
            self.result.initialize_with_num_den(numerator, self.fraction_a.denominator)
            return self.result
        numerator = (self.fraction_a.numerator * self.fraction_b.denominator) - (self.fraction_a.denominator * self.fraction_b.numerator)
        denominator = self.fraction_a.denominator * self.fraction_b.denominator
        self.result.initialize_with_num_den(numerator, denominator)
        return self.result
