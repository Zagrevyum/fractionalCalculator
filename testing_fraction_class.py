from Fraction import Fraction


sol = Fraction("3_2/4")

assert 14, 4 == (sol.num, sol.den)
assert "3_1/2" == sol.convert_to_string()

sol = Fraction("2/4")

assert (2, 4) == (sol.num, sol.den)
assert "1/2" == sol.convert_to_string()

sol = Fraction("16/4")
assert 16, 4 == (sol.num, sol.den)
assert "4" == sol.convert_to_string()

sol = Fraction("18/8")
assert 18, 8 == (sol.num, sol.den)
assert "2_1/4" == sol.convert_to_string()

sol2 = Fraction("")

assert (None, None) == (sol2.num, sol2.den)
sol2.initialize_with_num_den(2, 3)
assert "2/3" == sol2.convert_to_string()

