#usr/bin/python
import sys
from Calculator import Calculator
from Fraction import Fraction

def main(args : list):
    #operation = "? 1_3/2 * 3_3/4 * 1_1/4 +  5_11/24 / 3/2"

    index = 2
    while index < len(args)-1:
        fraction1 = Fraction(args[index-1])
        fraction2 = Fraction(args[index+1])
        operand = args[index]
        solved = Calculator(fraction1, fraction2)
        if operand == "*":
            result = solved.multiplication()
            args[index-1] = result.convert_to_string()
            args.pop(index)
            args.pop(index)
            index -= 2
        if operand == "/":
            result = solved.division()
            args[index - 1] = result.convert_to_string()
            args.pop(index)
            args.pop(index)
            index -= 2
        index += 2
    index = 2
    while index < len(args) - 1:
        fraction1 = Fraction(args[index - 1])
        fraction2 = Fraction(args[index + 1])
        operand = args[index]
        solved = Calculator(fraction1, fraction2)
        if operand == "+":
            result = solved.addition()
            args[index - 1] = result.convert_to_string()
            args.pop(index)
            args.pop(index)
            index -= 2
        if operand == "-":
            result = solved.subtraction()
            args[index - 1] = result.convert_to_string()
            args.pop(index)
            args.pop(index)
            index -= 2
        index += 2
    print(args[1])


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: Operands and operators shall be separated by one or more spaces Mixed numbers will be represented by whole_numerator/denominator. e.g. \"3_1/4\" " 
              "Improper fractions and whole numbers are also allowed as operands \n"
              "Example runs:\n"
              "? 1/2 * 3_3/4\n"
              "? 2_3/8 + 9/8\n")
        sys.exit(2)
    main(sys.argv)