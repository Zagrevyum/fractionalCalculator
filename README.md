# Fractional Calculator
Python command line program that will take operations on fractions as an input and produce a fractional result.
Usage:
# python main.py 3/4 + 5/8 * 3/5 - 8/9 / 3_5/7

Legal operators shall be *, /, +, - (multiply, divide, add, subtract)
Operands and operators shall be separated by one or more spaces
Mixed numbers will be represented by whole_numerator/denominator. e.g. "3_1/4"
Improper fractions and whole numbers are also allowed as operands
Note: doesn't handle negative fractions
Example runs:

 python main.py 1/2 * 3_3/4
= 1_7/8
 
 python main.py 2_3/8 + 9/8
= 3_1/2


# case for operator precedence

3/4 + 5/8 * 3/5 - 8/9 / 3_5/9 == 7/8

validation https://es.symbolab.com/solver/fractions-calculator/%5Cfrac%7B3%7D%7B4%7D%2B%5Cfrac%7B5%7D%7B8%7D%5Ccdot%5Cfrac%7B3%7D%7B5%7D-%5Cfrac%7B%5Cfrac%7B8%7D%7B9%7D%7D%7B3%20%5Cfrac%7B5%7D%7B9%7D%7D
