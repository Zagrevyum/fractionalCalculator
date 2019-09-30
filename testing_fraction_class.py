from Fraction import Fraction
import pytest
###validate parsing and simplication


##class with integer part and fractional part that can be simplified
sol = Fraction("3_2/4")

assert 14, 4 == (sol.numerator, sol.denominator)
assert "3_1/2" == sol.convert_to_string()


##simple fraction
sol = Fraction("2/4")

assert (2, 4) == (sol.numerator, sol.denominator)
assert "1/2" == sol.convert_to_string()


##improper fraction that results in just an integer part
sol = Fraction("16/4")
assert 16, 4 == (sol.numerator, sol.denominator)
assert "4" == sol.convert_to_string()

##improper fraction that results in an integer part with a fractional part that can be simplified
sol = Fraction("18/8")
assert 18, 8 == (sol.numerator, sol.denominator)
assert "2_1/4" == sol.convert_to_string()


##empty string for special cases
sol2 = Fraction("")

assert (None, None) == (sol2.numerator, sol2.denominator)
sol2.initialize_with_num_den(2, 3)
assert "2/3" == sol2.convert_to_string()

