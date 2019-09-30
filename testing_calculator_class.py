from Fraction import Fraction
from Calculator import Calculator
#case 1
frac1 = Fraction("1/2")
frac2 = Fraction("3_3/4")

result = Calculator(frac1, frac2).multiplication()

print(result.convert_to_string())

#case 2

frac1 = Fraction("2_3/8")
frac2 = Fraction("9/8")

result = Calculator(frac1, frac2).addition()

print(result.convert_to_string())