import sys
class Fraction:
    def __init__(self, fraction: str):
        self.num, self.den = self.convert_to_fraction(fraction)

    def convert_to_fraction(self, fraction: str):
        if fraction == "":
            return None, None
        integer_part = 0
        try:
            if fraction.find("_") != -1:
                integer_part = int(fraction.split("_")[0])
                fraction = fraction.split("_")[1]
            den = int(fraction.split("/")[1])
            if den == 0:
                print("Exception: Denominator can't be Zero")
                sys.exit(1)
            num = int(fraction.split("/")[0]) + integer_part*den
        except IndexError:
            print("wrong fraction format")
            sys.exit(1)
        return num, den

    def convert_to_string(self) -> str:
        fraction = ""
        self.simplify_fraction()
        integer_part = str(self.num // self.den) if self.num >= self.den else ""
        fractional_part = str(self.num % self.den)+"/"+str(self.den) if self.num % self.den > 0 else ""
        fraction += integer_part+"_" if integer_part != "" else ""
        fraction += fractional_part if fractional_part != "" else ""
        fraction = fraction.replace("_", "") if fractional_part == "" else fraction
        return fraction

    def simplify_fraction(self):
        common_divisor = 2
        while common_divisor < self.den:
            if self.den % common_divisor == 0 and self.num % common_divisor == 0:
                self.num //= common_divisor
                self.den //= common_divisor
                common_divisor = 1
            common_divisor += 1

    def initialize_with_num_den(self, num, den):
        self.num = num
        self.den = den
        if den == 0:
            print("Exception: Denominator can't be Zero")
            sys.exit(1)

