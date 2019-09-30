from Fraction import Fraction
from Calculator import Calculator
import main


##small cases
#case 1
frac1 = Fraction("1/2")
frac2 = Fraction("3_3/4")

result = Calculator(frac1, frac2).multiplication()

print(result.convert_to_string())

#case 2

frac1 = Fraction("2_2/3")
frac2 = Fraction("4")

result = Calculator(frac1, frac2).addition()
print(result.convert_to_string())

#case  3

frac1 = Fraction("4")
frac2 = Fraction("2/3")
result = Calculator(frac1, frac2).subtraction()
print(result.convert_to_string())

#case 4

frac1 = Fraction("2/3")
frac2 = Fraction("4")
result = Calculator(frac1, frac2).subtraction()
#print(result.numerator, result.denominator)
print(result.convert_to_string())


#case 5 == 3/4

frac1 = Fraction("3")
frac2 = Fraction("4")
result = Calculator(frac1, frac2).division()
print(result.convert_to_string())

#case 6 == -3/4
frac1 = Fraction("-1_1/2")
frac2 = Fraction("3/4")
result = Calculator(frac1, frac2).addition()
print(result.convert_to_string())

#case 6 ==0
frac1 = Fraction("-3/4")
frac2 = Fraction("3/4")
result = Calculator(frac1, frac2).addition()
print(result.convert_to_string())

#case for precedence priorities()
#3/4 + 5/8 * 3/5 - 8/9 / 3_5/9 == 7/8
#https://es.symbolab.com/solver/fractions-calculator/%5Cfrac%7B3%7D%7B4%7D%2B%5Cfrac%7B5%7D%7B8%7D%5Ccdot%5Cfrac%7B3%7D%7B5%7D-%5Cfrac%7B%5Cfrac%7B8%7D%7B9%7D%7D%7B3%20%5Cfrac%7B5%7D%7B9%7D%7D

#3/4 + 5/8 * 3/5 - 8/9 / 3_5/9 + -9/8== 1/4
#https://es.symbolab.com/solver/fractions-calculator/%5Cfrac%7B3%7D%7B4%7D%2B%5Cfrac%7B5%7D%7B8%7D%5Ccdot%5Cfrac%7B3%7D%7B5%7D-%5Cfrac%7B%5Cfrac%7B8%7D%7B9%7D%7D%7B3%20%5Cfrac%7B5%7D%7B9%7D%7D-%5Cfrac%7B9%7D%7B8%7D

#3/4 + 5/8 * -3/5 - 8/9 / 3_5/9 + -9/8 == -1
#https://es.symbolab.com/solver/fractions-calculator/%5Cfrac%7B3%7D%7B4%7D%2B%5Cfrac%7B5%7D%7B8%7D%5Ccdot%5Cfrac%7B-3%7D%7B5%7D-%5Cfrac%7B%5Cfrac%7B8%7D%7B9%7D%7D%7B3%20%5Cfrac%7B5%7D%7B9%7D%7D-%5Cfrac%7B9%7D%7B8%7D

#-1_1/2 + 3/4 + 5/8 * 3/5 - 8/9 / 3_5/9 == -5/8
#https://es.symbolab.com/solver/fractions-calculator/-1%5Cfrac%7B1%7D%7B2%7D%2B%5Cfrac%7B3%7D%7B4%7D%2B%5Cfrac%7B5%7D%7B8%7D%5Ccdot%5Cfrac%7B3%7D%7B5%7D-%5Cfrac%7B%5Cfrac%7B8%7D%7B9%7D%7D%7B3%20%5Cfrac%7B5%7D%7B9%7D%7D
