#class to process fraction properties, transform and simplify
import sys
#the fraction class takes a string and converts to numerator/denomintator fraction.

class Fraction:
    def __init__(self, fraction: str):
        self.numerator, self.denominator = self.convert_to_fraction(fraction)
    ## parses the string adding the integer part if existing to the fraction part returning integers -> numerator, denominator
    def convert_to_fraction(self, fraction: str):
        if fraction == "":
            return None, None
        integer_part = 0

        try:
            #returns improper fraction if only integer part
            if fraction.find("/") == -1:
                return int(fraction), 1
            #adds integer part to fraction part
            if fraction.find("_") != -1:
                fraction_parts = fraction.split("_")
                integer_part = int(fraction_parts[0])
                fraction = fraction_parts[1]
            denominator = int(fraction.split("/")[1])
            if denominator == 0:
                print("Exception: Denominator can't be Zero")
                sys.exit(1)
            numerator = int(fraction.split("/")[0]) + integer_part*denominator
        except IndexError:
            print("wrong fraction format")
            sys.exit(1)
        return numerator, denominator
##converts the denominator, numerator to a proper fraction with integer part(if required) and numerator/denominator simplified i.e 13/4 3_1/2
##doesnt handle negatives
    def convert_to_string(self) -> str:
        fraction = ""
        self.simplify_fraction()
        integer_part = str(self.numerator // self.denominator) if self.numerator >= self.denominator else ""
        fractional_part = str(self.numerator % self.denominator) + "/" + str(self.denominator) if self.numerator % self.denominator > 0 else ""
        fraction += integer_part + "_" if integer_part != "" else ""
        fraction += fractional_part if fractional_part != "" else ""
        fraction = fraction.replace("_", "") if fractional_part == "" else fraction
        return fraction
#simplifies the fraction to the lowest denominator possible
    def simplify_fraction(self):
        common_divisor = 2
        while common_divisor < self.denominator:
            if self.denominator % common_divisor == 0 and self.numerator % common_divisor == 0:
                self.numerator //= common_divisor
                self.denominator //= common_divisor
                common_divisor = 1
            common_divisor += 1
#method in case we want to initialize the fraction with denominator, numerator integers
    def initialize_with_num_den(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            print("Exception: Denominator can't be Zero")
            sys.exit(1)

