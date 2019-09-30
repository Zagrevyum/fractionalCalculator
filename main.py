#usr/bin/python
import sys
from Calculator import Calculator
from Fraction import Fraction


# resolve in place higher precedence operations returns a list with the operations
def resolve_higher_precedence_operations(operations: list) -> list:
    index = 2
    jump_to_operand = 2
    #I move in spaces of 2 because the operands are in pair directions as args starts in 1

    # maybe can use an additional stack to avoid the cost of the pop intermediate
    while index < len(operations) - 1:
        fraction1 = Fraction(operations[index - 1])
        fraction2 = Fraction(operations[index + 1])
        operand = operations[index]
        solved = Calculator(fraction1, fraction2)
        if operand == "*":
            result = solved.multiplication()
            operations[index - 1] = result.convert_to_string()
            operations.pop(index)
            operations.pop(index)
            index -= jump_to_operand
        if operand == "/":
            result = solved.division()
            operations[index - 1] = result.convert_to_string()
            operations.pop(index)
            operations.pop(index)
            index -= jump_to_operand
        index += jump_to_operand
    return operations


#takes the list of operations with only sums and rests and returns the final result
def resolve_lower_precedence_operations(operations: list) -> str:
    index = 2
    jump_to_operand = 2
    # I move in spaces of 2 because the operands are in pair directions as args starts in 1
    while index < len(operations) - 1:
        fraction1 = Fraction(operations[index - 1])
        fraction2 = Fraction(operations[index + 1])
        operand = operations[index]
        solved = Calculator(fraction1, fraction2)
        if operand == "+":
            result = solved.addition()
            operations[index - 1] = result.convert_to_string()
            operations.pop(index)
            operations.pop(index)
            index -= jump_to_operand
        if operand == "-":
            result = solved.subtraction()
            operations[index - 1] = result.convert_to_string()
            operations.pop(index)
            operations.pop(index)
            index -= jump_to_operand
        index += jump_to_operand
    return operations[1]

#method to parse parameters and resolve operations
def resolve_operations(operations: list) -> str:
#operation = "? 1_3/2 * 3_3/4 * 1_1/4 +  5_11/24 / 3/2"
    operations_to_resolve = resolve_higher_precedence_operations(operations)
    result = resolve_lower_precedence_operations(operations_to_resolve)
    return result


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: Operands and operators shall be separated by one or more spaces Mixed numbers will be represented by whole_numerator/denominator. e.g. \"3_1/4\" " 
              "Improper fractions and whole numbers are also allowed as operands \n"
              "Example runs:\n"
              "? 1/2 * 3_3/4\n"
              "? 2_3/8 + 9/8\n")
        sys.exit(2)
    print(resolve_operations(sys.argv))
