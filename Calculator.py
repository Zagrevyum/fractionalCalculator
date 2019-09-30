from Fraction import Fraction


class Calculator:
    def __init__(self, fractiona : Fraction, fractionb: Fraction):
        self.fractiona = fractiona
        self.fractionb = fractionb
        self.result = Fraction("")

    def multiplication(self) -> Fraction:
        num = self.fractiona.num * self.fractionb.num
        den = self.fractiona.den * self.fractionb.den
        self.result.initialize_with_num_den(num, den)
        return self.result

    def division(self) -> Fraction:
        num = self.fractiona.num * self.fractionb.den
        den = self.fractiona.den * self.fractionb.num
        self.result.initialize_with_num_den(num,den)
        return self.result

    def addition(self) -> Fraction:
        if self.fractiona.den == self.fractionb.den:
            num = self.fractiona.num + self.fractionb.num
            self.result.initialize_with_num_den(num, self.fractiona.den)
            return self.result
        num = (self.fractiona.num * self.fractionb.den) + (self.fractiona.den * self.fractionb.num)
        den = self.fractiona.den * self.fractionb.den
        self.result.initialize_with_num_den(num, den)
        return self.result

    def subtraction(self) -> Fraction:
        if self.fractiona.den == self.fractionb.den:
            num = self.fractiona.num - self.fractionb.num
            self.result.initialize_with_num_den(num, self.fractiona.den)
            return self.result
        num = (self.fractiona.num * self.fractionb.den) - (self.fractiona.den * self.fractionb.num)
        den = self.fractiona.den * self.fractionb.den
        self.result.initialize_with_num_den(num, den)
        return self.result



