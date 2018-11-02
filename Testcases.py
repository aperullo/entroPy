import unittest
from Float import Float
from Integer import Integer
from String import String
from Char import Char
import Settings

class TestFloatMethods(unittest.TestCase):

    #assertEquals actually has to rely on the float's implementation of __eq__ to work, so we need to test that first.
    def test__eq__(self):
        self.assertTrue(Float(1.0) == Float(1.0), "__eq__: comparing two Floats()")

        self.assertFalse(Float(1.0) == Float(2.0), "__eq__: comparing two Floats()")

        self.assertTrue(Float(1.0) == 1.0, "__eq__: comparing a Float() and a float")

        self.assertTrue(1.0 == Float(1.0), "__eq__: comparing a float and a Float()")

        self.assertFalse(Float(1.0) == 2.0, "__eq__: comparing a Float() and a float")

        self.assertFalse(2.0 == Float(1.0), "__eq__: comparing a float and a Float()")

    def test__ne__(self):
        self.assertFalse(Float(1.0) != Float(1.0), "__ne__: comparing two Floats()")

        self.assertTrue(Float(1.0) != Float(2.0), "__ne__: comparing two Floats()")

        self.assertFalse(Float(1.0) != 1.0, "__ne__: comparing a Float() and a float")

        self.assertFalse(1.0 != Float(1.0), "__ne__: comparing a float and a Float()")

        self.assertTrue(Float(1.0) != 2.0, "__ne__: comparing a Float() and a float")

        self.assertTrue(2.0 != Float(1.0), "__ne__: comparing a float and a Float()")

    def test__lt__(self):
        self.assertTrue(Float(1.0) < Float(2.0), "__lt__: comparing two Floats()")
        self.assertFalse(Float(1.0) < Float(1.0), "__lt__: comparing two Floats()")
        self.assertFalse(Float(2.0) < Float(1.0), "__lt__: comparing two Floats()")

        self.assertTrue(Float(1.0) < 2.0, "__lt__: comparing a Float() and a float")
        self.assertFalse(Float(1.0) < 1.0, "__lt__: comparing a Float() and a float")
        self.assertFalse(Float(2.0) < 1.0, "__lt__: comparing a Float() and a float")

        self.assertTrue(1.0 < Float(2.0), "__lt__: comparing a float and a Float()")
        self.assertFalse(1.0 < Float(1.0), "__lt__: comparing a float and a Float()")
        self.assertFalse(2.0 < Float(1.0), "__lt__: comparing a float and a Float()")

    def test__gt__(self):
        self.assertFalse(Float(1.0) > Float(2.0), "__gt__: comparing two Floats()")
        self.assertFalse(Float(1.0) > Float(1.0), "__gt__: comparing two Floats()")
        self.assertTrue(Float(2.0) > Float(1.0), "__gt__: comparing two Floats()")

        self.assertFalse(Float(1.0) > 2.0, "__gt__: comparing a Float() and a float")
        self.assertFalse(Float(1.0) > 1.0, "__gt__: comparing a Float() and a float")
        self.assertTrue(Float(2.0) > 1.0, "__gt__: comparing a Float() and a float")

        self.assertFalse(1.0 > Float(2.0), "__gt__: comparing a float and a Float()")
        self.assertFalse(1.0 > Float(1.0), "__gt__: comparing a float and a Float()")
        self.assertTrue(2.0 > Float(1.0), "__gt__: comparing a float and a Float()")

    def test__le__(self):
        self.assertTrue(Float(1.0) <= Float(2.0), "__le__: comparing two Floats()")
        self.assertTrue(Float(1.0) <= Float(1.0), "__le__: comparing two Floats()")
        self.assertFalse(Float(2.0) <= Float(1.0), "__le__: comparing two Floats()")

        self.assertTrue(Float(1.0) <= 2.0, "__le__: comparing a Float() and a float")
        self.assertTrue(Float(1.0) <= 1.0, "__le__: comparing a Float() and a float")
        self.assertFalse(Float(2.0) <= 1.0, "__le__: comparing a Float() and a float")

        self.assertTrue(1.0 <= Float(2.0), "__le__: comparing a float and a Float()")
        self.assertTrue(1.0 <= Float(1.0), "__le__: comparing a float and a Float()")
        self.assertFalse(2.0 <= Float(1.0), "__le__: comparing a float and a Float()")

    def test__ge__(self):
        self.assertFalse(Float(1.0) >= Float(2.0), "__ge__: comparing two Floats()")
        self.assertTrue(Float(1.0) >= Float(1.0), "__ge__: comparing two Floats()")
        self.assertTrue(Float(2.0) >= Float(1.0), "__ge__: comparing two Floats()")

        self.assertFalse(Float(1.0) >= 2.0, "__ge__: comparing a Float() and a float")
        self.assertTrue(Float(1.0) >= 1.0, "__ge__: comparing a Float() and a float")
        self.assertTrue(Float(2.0) >= 1.0, "__ge__: comparing a Float() and a float")

        self.assertFalse(1.0 >= Float(2.0), "__ge__: comparing a float and a Float()")
        self.assertTrue(1.0 >= Float(1.0), "__ge__: comparing a float and a Float()")
        self.assertTrue(2.0 >= Float(1.0), "__ge__: comparing a float and a Float()")

    def test_mutate(self):
        a = Float(1.0)
        # variable should be the same the first time its read
        self.assertEqual(a, 1.0)
        #variable should have changed after it was read once.
        self.assertNotEqual(a, 1.0, "_mutate: value didnt mutate")

    def test__str__(self):
        self.assertEqual(str(Float(1.0)), "1.0", "__str__: str()")

        self.assertEqual(Float(1.0).__str__(), "1.0", "__str__: __str__()")

        self.assertEqual(str(Float(1.0)), Float(1.0).__str__(), "__str__: compare str() to __str__()")

    def test__repr__(self):
        a = Float(1.0)  # since repr shouldn't mutate values we can use the same var in all tests

        self.assertEqual(repr(a), "Float(_val=1.0)", "__repr__: repr()")

        self.assertEqual(a.__repr__(), "Float(_val=1.0)", "__repr__: __repr__()")

        self.assertEqual(repr(a), a.__repr__(), "__repr__: compare repr() to __repr__()")

        self.assertEqual(a, 1.0, "__repr__: mutated value")  # test value is still 1.0 and hasn't mutated

    def test__index__(self):
        self.assertIs(Float(1.0).__index__(), 1, "__index__: not converting properly")

    def test__int__(self):
        self.assertIs(Float(1.0).__int__(), 1, "__int__: implicit conversion")
        self.assertIs(int(Float(1.0)), 1, "__int__: wrapper conversion")

    def test__float__(self):
        self.assertIsInstance(Float(1.0).__float__(), type(1.0), "__float__: implicit conversion")
        self.assertIsInstance(float(Float(1.0)), type(1.0), "__float__: wrapper conversion")

    def test__add__(self):
        self.assertEqual(Float(3.0) + Float(2.0), Float(5.0), "__add__: adding Float() to Float()")
        self.assertEqual(Float(3.0) + 2.0, Float(5.0), "__add__: adding Float() to float")

    def test__radd__(self):
        self.assertEqual(3.0 + Float(2.0), Float(5.0), "__radd__: adding float to Float()")

    def test__iadd__(self):
        Settings.MUTATION = False

        a = Float(1.0)
        a += Float(1.0)
        self.assertEqual(a._val, 2.0, "__iadd__: adding Float() to Float()")

        a += 1.0
        self.assertEqual(a._val, 3.0, "__iadd__: adding Float() to float")

        Settings.MUTATION = True

    def test__sub__(self):
        self.assertEqual(Float(3.0) - Float(2.0), Float(1.0), "__sub__: subtract Float() and Float()")
        self.assertEqual(Float(3.0) - 2.0, Float(1.0), "__sub__: subtract Float() and float")

    def test__rsub__(self):
        self.assertEqual(3.0 - Float(2.0), Float(1.0), "__rsub__: subtract float and Float()")

    def test__isub__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a -= Float(1.0)
        self.assertEqual(a._val, 2.0, "__isub__: subtract Float() and Float()")

        a -= 1.0
        self.assertEqual(a._val, 1.0, "__isub__: subtract Float() and float")

        Settings.MUTATION = True

    def test__mul__(self):
        self.assertEqual(Float(3.0) * Float(2.0), Float(6.0), "__mul__: multiply Float() and Float()")
        self.assertEqual(Float(3.0) * 2.0, Float(6.0), "__mul__: multiply Float() and float")

    def test__rmul__(self):
        self.assertEqual(3.0 * Float(2.0), Float(6.0), "__rmul__: multiply float and Float()")

    def test__imul__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a *= Float(2.0)
        self.assertEqual(a._val, 6.0, "__imul__: multiply Float() and Float()")

        a *= 2.0
        self.assertEqual(a._val, 12.0, "__imul__: multiply Float() and float")

        Settings.MUTATION = True

    def test__truediv__(self):
        self.assertEqual(Float(3.0) / Float(2.0), Float(1.5), "__truediv__(): divide Float() by Float()")
        self.assertEqual(Float(3.0) / 2.0, Float(1.5), "__truediv__(): divide Float() by float")
        self.assertRaises(ZeroDivisionError, lambda: (Float(3.0) / Float(0.0))) # lambda to be a callable division by zero

    def test__rtruediv__(self):
        self.assertEqual(3.0 / Float(2.0), Float(1.5), "__rtruediv__(): divide float by Float()")

    def test__itruediv__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a /= Float(2.0)
        self.assertEqual(a._val, 1.5, "__itruediv__(): divide Float() by Float()")

        self.assertRaises(ZeroDivisionError, lambda: a.__itruediv__(0))

        Settings.MUTATION = True

    def test__floordiv__(self):
        self.assertEqual(Float(3.0) // Float(2.0), Float(1.0), "__floordiv__(): divide Float() by Float()")
        self.assertEqual(Float(3.0) // 2.0, Float(1.0), "__floordiv__(): divide Float() by float")
        self.assertRaises(ZeroDivisionError, lambda: (Float(3.0) // Float(0.0))) # lambda to be a callable division by zero

    def test__rfloordiv__(self):
        self.assertEqual(3.0 // Float(2.0), Float(1.0), "__rfloordiv__(): divide float by Float()")

    def test__ifloordiv__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a //= Float(2.0)
        self.assertEqual(a._val, 1.0, "__ifloordiv__(): divide Float() by Float()")

        self.assertRaises(ZeroDivisionError, lambda: a.__ifloordiv__(0))

        Settings.MUTATION = True

    def test__mod__(self):
        self.assertEqual(Float(3.0) % Float(2.0), Float(1.0), "__mod__(): modulo Float() by Float()")
        self.assertEqual(Float(3.0) % 2.0, Float(1.0), "__mod__(): modulo Float() by float")
        self.assertRaises(ZeroDivisionError, lambda: (Float(3.0) % Float(0.0))) # lambda to be a callable division by zero

    def test__rmod__(self):
        self.assertEqual(3.0 % Float(2.0), Float(1.0), "__rmod__(): modulo float by Float()")

    def test__imod__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a %= Float(2.0)
        self.assertEqual(a._val, 1.0, "__imod__(): modulo Float() by Float()")

        self.assertRaises(ZeroDivisionError, lambda: a.__mod__(0))

        Settings.MUTATION = True

    def test__divmod__(self):
        self.assertEqual(divmod(Float(3.0), Float(2.0)), (Float(1.0), Float(1.0)), "__divmod__():  modulo Float() by Float()")
        self.assertEqual(divmod(Float(3.0), 2.0), (Float(1.0), Float(1.0)), "__divmod__():  modulo Float() by float")
        self.assertRaises(ZeroDivisionError, lambda: divmod(Float(3.0), Float(0.0))) # lambda to be a callable division by zero

    def test__rdivmod__(self):
        self.assertEqual(divmod(3.0, Float(2.0)), (Float(1.0), Float(1.0)), "__rdivmod__(): modulo float by Float()")

    def test__pow__(self):
        self.assertEqual(Float(3.0) ** Float(2.0), Float(9.0), "__pow__(): Float() Raised to Float()")
        self.assertEqual(Float(3.0) ** 2.0, Float(9.0), "__pow__(): Float() Raised to float")

    def test__rpow__(self):
        self.assertEqual(3.0 ** Float(2.0), Float(9.0), "__rpow__(): float Raised to Float()")

    def test__ipow__(self):
        Settings.MUTATION = False

        a = Float(3.0)
        a **= Float(2.0)
        self.assertEqual(a._val, 9.0, "__ipow__(): Float() Raised to Float()")

        a **= 2.0
        self.assertEqual(a._val, 81.0, "__ipow__(): Float() Raised to float")

        Settings.MUTATION = True

    def test__neg__(self):
        self.assertEqual(Float(1.0).__neg__(), Float(-1.0), "__neg__(): -pos -> neg")

        self.assertEqual(Float(-1.0).__neg__(), Float(1.0), "__neg__(): -neg -> pos")

    #unary plus is basically a no-op
    def test__pos__(self):
        self.assertEqual(Float(1.0).__pos__(), Float(1.0), "__pos__(): +pos -> pos")

        self.assertEqual(Float(-1.0).__pos__(), Float(-1.0), "__pos__(): +neg -> neg")

    def test__abs__(self):
        self.assertEqual(Float(1.0).__abs__(), Float(1.0), "__abs__(): |pos| -> pos")

        self.assertEqual(Float(-1.0).__abs__(), Float(1.0), "__abs__(): |neg| -> pos")

    def test__round__(self):
        self.assertEqual(Float(1.123456).__round__(2), Float(1.12), "__round__(): rounding to 2 figures")
        self.assertEqual(Float(1.123456).__round__(5), Float(1.12346), "__round__(): rounding up to 5")
        self.assertEqual(Float(1.123456).__round__(9), Float(1.123456), "__round__(): rounding to more places than available")
        self.assertEqual(Float(1.123456).__round__(0), Float(1.0), "__round__(): rounding to 0 places")
        self.assertEqual(Float(1.123456).__round__(-1), Float(0.0), "__round__(): rounding to negative places")

    def test__trunc__(self):
        self.assertEqual(Float(1.123456).__trunc__(), Integer(1), "__trunc__(): trunc(pos) -> pos int")
        self.assertEqual(Float(-1.123456).__trunc__(), Integer(-1), "__trunc__(): trunc(neg) -> neg int")
        self.assertEqual(Float(0.0).__trunc__(), Integer(0), "__trunc__(): trunc(0.0) -> 0")


class TestIntegerMethods(unittest.TestCase):

    #assertEquals actually has to rely on the Integer's implementation of __eq__ to work, so we need to test that first.
    def test__eq__(self):
        a = Integer(1)
        self.assertTrue(Integer(1) == Integer(1), "__eq__: comparing two Integers()")

        self.assertFalse(Integer(1) == Integer(2), "__eq__: comparing two Floats()")

        self.assertTrue(Integer(1) == 1, "__eq__: comparing a Integer() and a int")

        self.assertTrue(1 == Integer(1), "__eq__: comparing a float and a Integer()")

        self.assertFalse(Integer(1) == 2, "__eq__: comparing a Integer() and a int")

        self.assertFalse(2 == Integer(1), "__eq__: comparing a int and a Integer()")

        self.assertTrue(Integer(1) == Float(1.0), "__eq__: comparing Integer and a Float()")

        self.assertTrue(Integer(1) == 1.0, "__eq__: comparing Integer() and float")

    def test__ne__(self):
        self.assertFalse(Integer(1) != Integer(1), "__ne__: comparing two ints()")

        self.assertTrue(Integer(1) != Integer(2), "__ne__: comparing two ints()")

        self.assertFalse(Integer(1) != 1, "__ne__: comparing a Integer() and a int")

        self.assertFalse(1 != Integer(1), "__ne__: comparing a int and a Integer()")

        self.assertTrue(Integer(1) != 2, "__ne__: comparing a Integer() and a int")

        self.assertTrue(2 != Integer(1), "__ne__: comparing a int and a Integer()")

        self.assertFalse(Integer(1) != Float(1.0), "__eq__: comparing Integer and a Float()")

        self.assertFalse(Integer(1) != 1.0, "__eq__: comparing Integer() and float")

    def test__lt__(self):
        self.assertTrue(Integer(1) < Integer(2), "__lt__: comparing two Integers()")
        self.assertFalse(Integer(1) < Integer(1), "__lt__: comparing two Integers()")
        self.assertFalse(Integer(2) < Integer(1), "__lt__: comparing two Integers()")

        self.assertTrue(Integer(1) < 2, "__lt__: comparing an Integer() and an int")
        self.assertFalse(Integer(1) < 1, "__lt__: comparing an Integer() and an int")
        self.assertFalse(Integer(2) < 1, "__lt__: comparing an Integer() and an int")

        self.assertTrue(1 < Integer(2), "__lt__: comparing an int and an Integer()")
        self.assertFalse(1 < Integer(1), "__lt__: comparing an int and an Integer()")
        self.assertFalse(2 < Integer(1), "__lt__: comparing an int and an Integer()")

        self.assertTrue(Integer(1) < Float(2.0), "__lt__: comparing an Integer() and a Float()")
        self.assertFalse(Integer(1) < Float(1.0), "__lt__: comparing an Integer() and a Float()")
        self.assertFalse(Integer(2) < Float(1.0), "__lt__: comparing an Integer() and a Float()")

        self.assertTrue(Integer(1) < 2.0, "__lt__: comparing an Integer() and a float")
        self.assertFalse(Integer(1) < 1.0, "__lt__: comparing an Integer() and a float")
        self.assertFalse(Integer(2) < 1.0, "__lt__: comparing an Integer() and a float")

    def test__gt__(self):
        self.assertFalse(Integer(1) > Integer(2), "__gt__: comparing two Integers()")
        self.assertFalse(Integer(1) > Integer(1), "__gt__: comparing two Integers()")
        self.assertTrue(Integer(2) > Integer(1), "__gt__: comparing two Integers()")

        self.assertFalse(Integer(1) > 2, "__gt__: comparing an Integer() and an int")
        self.assertFalse(Integer(1) > 1, "__gt__: comparing an Integer() and an int")
        self.assertTrue(Integer(2) > 1, "__gt__: comparing an Integer() and an int")

        self.assertFalse(1 > Integer(2), "__gt__: comparing an int and an Integer()")
        self.assertFalse(1 > Integer(1), "__gt__: comparing an int and an Integer()")
        self.assertTrue(2 > Integer(1), "__gt__: comparing an int and an Integer()")

        self.assertFalse(Integer(1) > Float(2.0), "__lt__: comparing an Integer() and a Float()")
        self.assertFalse(Integer(1) > Float(1.0), "__lt__: comparing an Integer() and a Float()")
        self.assertTrue(Integer(2) > Float(1.0), "__lt__: comparing an Integer() and a Float()")

        self.assertFalse(Integer(1) > 2.0, "__lt__: comparing an Integer() and a float")
        self.assertFalse(Integer(1) > 1.0, "__lt__: comparing an Integer() and a float")
        self.assertTrue(Integer(2) > 1.0, "__lt__: comparing an Integer() and a float")

    def test__le__(self):
        self.assertTrue(Integer(1) <= Integer(2), "__le__: comparing two Integers()")
        self.assertTrue(Integer(1) <= Integer(1), "__le__: comparing two Integers()")
        self.assertFalse(Integer(2) <= Integer(1), "__le__: comparing two Integers()")

        self.assertTrue(Integer(1) <= 2, "__le__: comparing an Integer() and an int")
        self.assertTrue(Integer(1) <= 1, "__le__: comparing an Integer() and an int")
        self.assertFalse(Integer(2) <= 1, "__le__: comparing an Integer() and an int")

        self.assertTrue(1 <= Integer(2), "__le__: comparing an int and an Integer()")
        self.assertTrue(1 <= Integer(1), "__le__: comparing an int and an Integer()")
        self.assertFalse(2 <= Integer(1), "__le__: comparing an int and an Integer()")

        self.assertTrue(Integer(1) <= Float(2.0), "__lt__: comparing an Integer() and a Float()")
        self.assertTrue(Integer(1) <= Float(1.0), "__lt__: comparing an Integer() and a Float()")
        self.assertFalse(Integer(2) <= Float(1.0), "__lt__: comparing an Integer() and a Float()")

        self.assertTrue(Integer(1) <= 2.0, "__lt__: comparing an Integer() and a float")
        self.assertTrue(Integer(1) <= 1.0, "__lt__: comparing an Integer() and a float")
        self.assertFalse(Integer(2) <= 1.0, "__lt__: comparing an Integer() and a float")

    def test__ge__(self):
        self.assertFalse(Integer(1) >= Integer(2), "__ge__: comparing two Integers()")
        self.assertTrue(Integer(1) >= Integer(1), "__ge__: comparing two Integers()")
        self.assertTrue(Integer(2) >= Integer(1), "__ge__: comparing two Integers()")

        self.assertFalse(Integer(1) >= 2, "__ge__: comparing an Integer() and an int")
        self.assertTrue(Integer(1) >= 1, "__ge__: comparing an Integer() and an int")
        self.assertTrue(Integer(2) >= 1, "__ge__: comparing an Integer() and an int")

        self.assertFalse(1 >= Integer(2), "__ge__: comparing an int and an Integer()")
        self.assertTrue(1 >= Integer(1), "__ge__: comparing an int and an Integer()")
        self.assertTrue(2 >= Integer(1), "__ge__: comparing an int and an Integer()")

        self.assertFalse(Integer(1) >= Float(2.0), "__lt__: comparing an Integer() and a Float()")
        self.assertTrue(Integer(1) >= Float(1.0), "__lt__: comparing an Integer() and a Float()")
        self.assertTrue(Integer(2) >= Float(1.0), "__lt__: comparing an Integer() and a Float()")

        self.assertFalse(Integer(1) >= 2.0, "__lt__: comparing an Integer() and a float")
        self.assertTrue(Integer(1) >= 1.0, "__lt__: comparing an Integer() and a float")
        self.assertTrue(Integer(2) >= 1.0, "__lt__: comparing an Integer() and a float")

    def test_mutate(self):
        a = Integer(5)
        # variable should be the same the first time its read
        self.assertEqual(a, 5)
        int(a)
        int(a)
        # variable should have changed after it was read several times.
        self.assertNotEqual(a, 5, "_mutate: value didnt mutate")

    def test__str__(self):
        self.assertEqual(str(Integer(1)), "1", "__str__: str()")

        self.assertEqual(Integer(1).__str__(), "1", "__str__: __str__()")

        self.assertEqual(str(Integer(1)), Integer(1).__str__(), "__str__: compare str() to __str__()")

    def test__repr__(self):
        a = Integer(1)  # since repr shouldn't mutate values we can use the same var in all tests

        self.assertEqual(repr(a), "Integer(_val=1)", "__repr__: repr()")

        self.assertEqual(a.__repr__(), "Integer(_val=1)", "__repr__: __repr__()")

        self.assertEqual(repr(a), a.__repr__(), "__repr__: compare repr() to __repr__()")

        self.assertEqual(a, 1, "__repr__: mutated value")  # test value is still 1 and hasn't mutated

    def test__index__(self):
        self.assertIs(Integer(1).__index__(), 1, "__index__: not converting properly")

    def test__int__(self):
        self.assertIs(Integer(1).__int__(), 1, "__int__: implicit conversion")
        self.assertIs(int(Integer(1)), 1, "__int__: wrapper conversion")

    def test__float__(self):
        self.assertIsInstance(Integer(1).__float__(), type(1.0), "__float__: implicit conversion")
        self.assertIsInstance(float(Integer(1)), type(1.0), "__float__: wrapper conversion")


    def test__add__(self):
        self.assertEqual(Integer(3) + Integer(2), Integer(5), "__add__: adding Integer() to Integer()")
        self.assertEqual(Integer(3) + 2, Integer(5), "__add__: adding Integer() to int")

    def test__radd__(self):
        self.assertEqual(3 + Integer(2), Integer(5), "__radd__: adding int to Integer()")

    def test__iadd__(self):
        Settings.MUTATION = False

        a = Integer(1)
        a += Integer(1)
        self.assertEqual(a._val, 2, "__iadd__: adding Integer() to Integer()")

        a += 1
        self.assertEqual(a._val, 3, "__iadd__: adding Integer() to int")

        Settings.MUTATION = True

    def test__sub__(self):
        self.assertEqual(Integer(3) - Integer(2), Integer(1), "__sub__: subtract Integer() and Integer()")
        self.assertEqual(Integer(3) - 2, Integer(1), "__sub__: subtract Integer() and int")

    def test__rsub__(self):
        self.assertEqual(3 - Integer(2), Integer(1), "__rsub__: subtract int and Integer()")

    def test__isub__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a -= Integer(1)
        self.assertEqual(a._val, 2, "__isub__: subtract Integer() and Integer()")

        a -= 1
        self.assertEqual(a._val, 1, "__isub__: subtract Integer() and int")

        Settings.MUTATION = True

    def test__mul__(self):
        self.assertEqual(Integer(3) * Integer(2), Integer(6), "__mul__: multiply Integer() and Integer()")
        self.assertEqual(Integer(3) * 2, Integer(6), "__mul__: multiply Integer() and int")

    def test__rmul__(self):
        self.assertEqual(3 * Integer(2), Integer(6), "__rmul__: multiply int and Integer()")

    def test__imul__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a *= Integer(2)
        self.assertEqual(a.val, 6, "__imul__: multiply Integer() and Integer()")

        a *= 2.0
        self.assertEqual(a.val, 12, "__imul__: multiply Integer() and int")

        Settings.MUTATION = True

    def test__truediv__(self):
        a = Integer(3) / Integer(2)
        self.assertEqual(a, Float(1.5), "__truediv__(): divide Integer() by Integer()")
        self.assertIsInstance(a, type(Float(1.5)), "__truediv__(): divide Integer() by Integer()")

        b = Integer(3) / 2
        self.assertEqual(b, Float(1.5), "__truediv__(): divide Integer() by int")
        self.assertIsInstance(b, type(Float(1.5)), "__truediv__(): divide Integer() by int()")

        self.assertRaises(ZeroDivisionError, lambda: (Integer(3) / Integer(0)))  # lambda to be an callable division by zero

    def test__rtruediv__(self):
        a = 3 / Integer(2)
        self.assertEqual(a, Float(1.5), "__rtruediv__(): divide float by Integer()")
        self.assertIsInstance(a, type(Float(1.5)), "__rtruediv__(): divide float by Integer()")

    def test__itruediv__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a /= Integer(2)
        self.assertEqual(a.val, Float(1.5), "__itruediv__(): divide Integer() by Integer()")
        self.assertIsInstance(a, type(Float(1.5)), "__itruediv__(): divide Integer() by Integer()")

        self.assertRaises(ZeroDivisionError, lambda: a.__itruediv__(0))

        Settings.MUTATION = True

    def test__floordiv__(self):
        self.assertEqual(Integer(3) // Integer(2), Integer(1), "__floordiv__(): divide Integer() by Integer()")
        self.assertEqual(Integer(3) // 2, Integer(1), "__floordiv__(): divide Integer() by int")
        self.assertIsInstance(Integer(3) // Integer(2), type(Integer(1)))
        self.assertRaises(ZeroDivisionError, lambda: (Integer(3) // Integer(0)))  # lambda to be an callable division by zero

    def test__rfloordiv__(self):
        a = 3 // Integer(2)
        self.assertEqual(a, Integer(1), "__rfloordiv__(): divide int by Integer()")
        self.assertIsInstance(a, type(Integer(1)), "__rfloordiv__(): divide int by Integer()")

    def test__ifloordiv__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a //= Integer(2)
        self.assertEqual(a.val, 1, "__ifloordiv__(): divide Integer() by Integer()")
        self.assertIsInstance(a, type(Integer(1)), "__truediv__(): divide Integer() by Integer()")
        self.assertRaises(ZeroDivisionError, lambda: a.__ifloordiv__(0))

        Settings.MUTATION = True

    def test__mod__(self):
        self.assertEqual(Integer(3) % Integer(2), Integer(1), "__mod__(): modulo Integer() by Integer()")
        self.assertEqual(Integer(3) % 2, Integer(1), "__mod__(): modulo Integer() by float")
        self.assertRaises(ZeroDivisionError,
                          lambda: (Integer(3) % Integer(0)))  # lambda to be an callable division by zero

    def test__rmod__(self):
        self.assertEqual(3 % Integer(2), Integer(1), "__rmod__(): modulo float by Integer()")

    def test__imod__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a %= Integer(2)
        self.assertEqual(a.val, 1, "__imod__(): modulo Integer() by Integer()")
        self.assertIsInstance(a, type(Integer(1)), "__imod__(): modulo Integer() by Integer()")

        self.assertRaises(ZeroDivisionError, lambda: a.__imod__(0))

        Settings.MUTATION = True

    def test__divmod__(self):
        self.assertEqual(divmod(Integer(3), Integer(2)), (Integer(1), Integer(1)),
                         "__divmod__():  modulo Integer() by Integer()")
        self.assertEqual(divmod(Integer(3), 2), (Integer(1), Integer(1)), "__divmod__():  modulo Integer() by float")
        self.assertRaises(ZeroDivisionError,
                          lambda: divmod(Integer(3), Integer(0)))  # lambda to be an callable division by zero

    def test__rdivmod__(self):
        self.assertEqual(divmod(3, Integer(2)), (Integer(1), Integer(1)), "__rdivmod__(): modulo float by Integer()")

    def test__pow__(self):
        self.assertEqual(Integer(3) ** Integer(2), Integer(9), "__pow__(): Integer() Raised to Integer()")
        self.assertEqual(Integer(3) ** 2, Integer(9), "__pow__(): Integer() Raised to int")

    def test__rpow__(self):
        self.assertEqual(3 ** Integer(2), Integer(9), "__rpow__(): int Raised to Integer()")

    def test__ipow__(self):
        Settings.MUTATION = False

        a = Integer(3)
        a **= Integer(2)
        self.assertEqual(a._val, 9, "__ipow__(): Integer() Raised to Integer()")

        a **= 2
        self.assertEqual(a._val, 81, "__ipow__(): Integer() Raised to int")

        Settings.MUTATION = True

    def test__neg__(self):
        self.assertEqual(Integer(1).__neg__(), Integer(-1), "__neg__(): -pos -> neg")

        self.assertEqual(Integer(-1).__neg__(), Integer(1), "__neg__(): -neg -> pos")

    # unary plus is basically an no-op
    def test__pos__(self):
        self.assertEqual(Integer(1).__pos__(), Integer(1), "__pos__(): +pos -> pos")

        self.assertEqual(Integer(-1).__pos__(), Integer(-1), "__pos__(): +neg -> neg")

    def test__abs__(self):
        self.assertEqual(Integer(1).__abs__(), Integer(1), "__abs__(): |pos| -> pos")

        self.assertEqual(Integer(-1).__abs__(), Integer(1), "__abs__(): |neg| -> pos")

    def test__round__(self):
        self.assertEqual(Integer(1.123456).__round__(2), Integer(1.12), "__round__(): rounding to 2 figures")
        self.assertEqual(Integer(1.123456).__round__(5), Integer(1.12346), "__round__(): rounding up to 5")
        self.assertEqual(Integer(1.123456).__round__(9), Integer(1.123456), "__round__(): rounding to more places than available")
        self.assertEqual(Integer(1.123456).__round__(0), Integer(1), "__round__(): rounding to 0 places")
        self.assertEqual(Integer(1.123456).__round__(-1), Integer(0), "__round__(): rounding to negative places")

    def test__trunc__(self):
        self.assertEqual(Integer(1.123456).__trunc__(), Integer(1), "__trunc__(): trunc(pos) -> pos int")
        self.assertEqual(Integer(-1.123456).__trunc__(), Integer(-1), "__trunc__(): trunc(neg) -> neg int")
        self.assertEqual(Integer(0).__trunc__(), Integer(0), "__trunc__(): trunc(0) -> 0")


class TestCharMethods(unittest.TestCase):
    # assertEquals actually has to rely on the Char's implementation of __eq__ to work, so we need to test that first.
    def test__eq__(self):
        self.assertTrue(Char("A") == Char("A"), "__eq__: comparing two Char()")

        self.assertFalse(Char("A") == Char("B"), "__eq__: comparing two Char()")

        self.assertTrue(Char("A") == "A", "__eq__: comparing a Char() and a string")

        self.assertTrue("A" == Char("A"), "__eq__: comparing a string and a Char()")

        self.assertFalse(Char("A") == "B", "__eq__: comparing a Char() and a string")

        self.assertFalse("B" == Char("A"), "__eq__: comparing a string and a Char()")

    def test__ne__(self):
        self.assertFalse(Char("A") != Char("A"), "__eq__: comparing two Char()")

        self.assertTrue(Char("A") != Char("B"), "__eq__: comparing two Char()")

        self.assertFalse(Char("A") != "A", "__eq__: comparing a Char() and a string")

        self.assertFalse("A" != Char("A"), "__eq__: comparing a string and a Char()")

        self.assertTrue(Char("A") != "B", "__eq__: comparing a Char() and a string")

        self.assertTrue("B" != Char("A"), "__eq__: comparing a string and a Char()")

    def test_mutate(self):
        a = Char("a")
        # variable should be the same the first time its read
        self.assertEqual(a, "a")

        #since chars drift slowly, 1 read will not guaruntee a change.
        for x in range(100):
            a.__str__()

        #char may still be "a" after read, but its val is extremely unlikely to still be 97.
        self.assertNotEqual(a._val, 97, "_mutate: value didnt mutate")

    def test__str__(self):
        self.assertEqual(str(Char("A")), "A", "__str__: str()")

        self.assertEqual(Char("A").__str__(), "A", "__str__: __str__()")

        self.assertEqual(str(Char("A")), Char("A").__str__(), "__str__: compare str() to __str__()")

    #used to create a debugging view of a char, but some things called repr instead of str, so we have to make them function the same.
    def test__repr__(self):

        self.assertEqual(str(Char("A")), "A", "__str__: str()")

        self.assertEqual(Char("A").__str__(), "A", "__str__: __str__()")

        self.assertEqual(str(Char("A")), Char("A").__str__(), "__str__: compare str() to __str__()")

        # a = Char("A")  # since repr shouldn't mutate values we can use the same var in all tests

        # self.assertEqual(a.__repr__(), "Char(_val='A')", "__repr__: __repr__()")
        #
        # self.assertEqual(repr(a), a.__repr__(), "__repr__: compare repr() to __repr__()")
        #
        # self.assertEqual(a, "A", "__repr__: mutated value")  # test value is still "Aa" and hasn't mutated
        # self.assertEqual(repr(a), "Char(_val='A')", "__repr__: repr()")

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        Settings.MUTATION = False
        pass

    def tearDown(self):
        Settings.MUTATION = True
        pass

    # assertEquals actually has to rely on the String's implementation of __eq__ to work, so we need to test that first.
    def test__eq__(self):
        self.assertTrue(String("Aa") == String("Aa"), "__eq__: comparing two Strings()")

        self.assertFalse(String("Aa") == String("Bb"), "__eq__: comparing two Strings()")

        self.assertTrue(String("Aa") == "Aa", "__eq__: comparing a String() and a string")

        self.assertTrue("Aa" == String("Aa"), "__eq__: comparing a string and a String()")

        self.assertFalse(String("Aa") == "Bb", "__eq__: comparing a String() and a string")

        self.assertFalse("Bb" == String("Aa"), "__eq__: comparing a string and a String()")

    def test__ne__(self):
        self.assertFalse(String("Aa") != String("Aa"), "__ne__: comparing two Strings()")

        self.assertTrue(String("Aa") != String("Bb"), "__ne__: comparing two Strings()")

        self.assertFalse(String("Aa") != "Aa", "__ne__: comparing a String() and a string")

        self.assertFalse("Aa" != String("Aa"), "__ne__: comparing a string and a String()")

        self.assertTrue(String("Aa") != "Bb", "__ne__: comparing a String() and a string")

        self.assertTrue("Bb" != String("Aa"), "__ne__: comparing a string and a String()")

    def test__lt__(self):
        self.assertTrue(String("Aa") < String("Bb"), "__lt__: comparing two Strings()")
        self.assertFalse(String("Aa") < String("Aa"), "__lt__: comparing two Strings()")
        self.assertFalse(String("Bb") < String("Aa"), "__lt__: comparing two Strings()")

        self.assertTrue(String("Aa") < "Bb", "__lt__: comparing a String() and a string")
        self.assertFalse(String("Aa") < "Aa", "__lt__: comparing a String() and a string")
        self.assertFalse(String("Bb") < "Aa", "__lt__: comparing a String() and a string")

        self.assertTrue("Aa" < String("Bb"), "__lt__: comparing a string and a String()")
        self.assertFalse("Aa" < String("Aa"), "__lt__: comparing a string and a String()")
        self.assertFalse("Bb" < String("Aa"), "__lt__: comparing a string and a String()")

    def test__gt__(self):
        self.assertFalse(String("Aa") > String("Bb"), "__gt__: comparing two Strings()")
        self.assertFalse(String("Aa") > String("Aa"), "__gt__: comparing two Strings()")
        self.assertTrue(String("Bb") > String("Aa"), "__gt__: comparing two Strings()")

        self.assertFalse(String("Aa") > "Bb", "__gt__: comparing a String() and a string")
        self.assertFalse(String("Aa") > "Aa", "__gt__: comparing a String() and a string")
        self.assertTrue(String("Bb") > "Aa", "__gt__: comparing a String() and a string")

        self.assertFalse("Aa" > String("Bb"), "__gt__: comparing a string and a String()")
        self.assertFalse("Aa" > String("Aa"), "__gt__: comparing a string and a String()")
        self.assertTrue("Bb" > String("Aa"), "__gt__: comparing a string and a String()")

    def test__le__(self):
        self.assertTrue(String("Aa") <= String("Bb"), "__le__: comparing two Strings()")
        self.assertTrue(String("Aa") <= String("Aa"), "__le__: comparing two Strings()")
        self.assertFalse(String("Bb") <= String("Aa"), "__le__: comparing two Strings()")

        self.assertTrue(String("Aa") <= "Bb", "__le__: comparing a String() and a string")
        self.assertTrue(String("Aa") <= "Aa", "__le__: comparing a String() and a string")
        self.assertFalse(String("Bb") <= "Aa", "__le__: comparing a String() and a string")

        self.assertTrue("Aa" <= String("Bb"), "__le__: comparing a string and a String()")
        self.assertTrue("Aa" <= String("Aa"), "__le__: comparing a string and a String()")
        self.assertFalse("Bb" <= String("Aa"), "__le__: comparing a string and a String()")

    def test__ge__(self):
        self.assertFalse(String("Aa") >= String("Bb"), "__ge__: comparing two Strings()")
        self.assertTrue(String("Aa") >= String("Aa"), "__ge__: comparing two Strings()")
        self.assertTrue(String("Bb") >= String("Aa"), "__ge__: comparing two Strings()")

        self.assertFalse(String("Aa") >= "Bb", "__ge__: comparing a String() and a string")
        self.assertTrue(String("Aa") >= "Aa", "__ge__: comparing a String() and a string")
        self.assertTrue(String("Bb") >= "Aa", "__ge__: comparing a String() and a string")

        self.assertFalse("Aa" >= String("Bb"), "__ge__: comparing a string and a String()")
        self.assertTrue("Aa" >= String("Aa"), "__ge__: comparing a string and a String()")
        self.assertTrue("Bb" >= String("Aa"), "__ge__: comparing a string and a String()")

    def test__contains__(self):
        self.assertTrue(String("abcde").__contains__(String("a")))
        self.assertTrue(String("a") in String("abcde"))
        self.assertTrue(String("abcde").__contains__("a"))
        self.assertTrue("a" in String("abcde"))

        self.assertTrue(String("abcde").__contains__(String("ab")))
        self.assertTrue(String("ab") in String("abcde"))
        self.assertTrue(String("abcde").__contains__("ab"))
        self.assertTrue("ab" in String("abcde"))

        self.assertFalse(String("bcde").__contains__(String("a")))
        self.assertFalse(String("a") in String("bcde"))
        self.assertFalse(String("bcde").__contains__("a"))
        self.assertFalse("a" in String("bcde"))

        self.assertFalse(String("abcde").__contains__(String("ac")))
        self.assertFalse(String("ac") in String("abcde"))
        self.assertFalse(String("abcde").__contains__("ac"))
        self.assertFalse("ac" in String("abcde"))

    def test__str__(self):
        self.assertEqual(str(String("Aa")), "Aa", "__str__: str()")

        self.assertEqual(String("Aa").__str__(), "Aa", "__str__: __str__()")

        self.assertEqual(str(String("Aa")), String("Aa").__str__(), "__str__: compare str() to __str__()")

    def test__repr__(self):
        self.assertEqual(str(String("Aa")), "Aa", "__str__: str()")

        self.assertEqual(String("Aa").__str__(), "Aa", "__str__: __str__()")

        self.assertEqual(str(String("Aa")), String("Aa").__str__(), "__str__: compare str() to __str__()")

        # a = String("Aa")  # since repr shouldn't mutate values we can use the same var in all tests
        #
        # self.assertEqual(repr(a), "String(_chars=(Char(_val='A'), Char(_val='a')))", "__repr__: repr()")
        #
        # self.assertEqual(a.__repr__(), "String(_chars=(Char(_val='A'), Char(_val='a')))", "__repr__: __repr__()")
        #
        # self.assertEqual(repr(a), a.__repr__(), "__repr__: compare repr() to __repr__()")
        #
        # self.assertEqual(a, "Aa", "__repr__: mutated value")  # test value is still "Aa" and hasn't mutated

    def test__len__(self):
        a = (len(String("abcd")))
        self.assertEqual(a, Integer(4), "__len__: length did not match")
        self.assertIsInstance(a, int, "__len__: did not return an Int")

    def test_capitalize(self):
        self.assertEqual(String("abcde").capitalize(), "Abcde")
        self.assertEqual(String("ABCDE").capitalize(), "Abcde")
        self.assertEqual(String("Ab cde").capitalize(), "Ab cde")
        self.assertEqual(String(" ").capitalize(), " ")
        self.assertEqual(String("").capitalize(), "")

    def test_casefold(self):
        self.assertEqual(String("abcde").casefold(), "abcde")
        self.assertEqual(String("ABCDE").casefold(), "abcde")
        self.assertEqual(String("Ab cde").casefold(), "ab cde")
        self.assertEqual(String(" ").casefold(), " ")
        self.assertEqual(String("").casefold(), "")

    def test_center(self):
        self.assertEqual(String("abcde").center(10, " "), "  abcde   ")
        self.assertEqual(String("ABCDE").center(5, "-"), "ABCDE")
        self.assertEqual(String("Ab cde").center(10, "-"), "--Ab cde--")
        self.assertEqual(String(" ").center(9, "-"), "---- ----")
        self.assertEqual(String("").center(10, " "), "          ")

    def test_count(self):
        self.assertEqual(String("abcde").count(String("a")), 1)
        self.assertEqual(String("ABCDE").count("f"), 0)
        self.assertEqual(String("cabcdec").count("c"), 3)
        self.assertEqual(String("cabcdec").count("c", 1, 6), 1)
        self.assertEqual(String("").count(""), 1)

    #todo: doesn't work because Chars only accept certain characters, and tab isn't one of them.
    def test_expandtabs(self):
        #self.assertEqual(String("\t abcde").expandtabs(), "         abcde")
        #self.assertEqual(String("\tabcde").expandtabs(tabsize=4), "    abcde")
        pass

    def test_index(self):
        self.assertEqual(String("abcde").index(String("a")), 0)
        self.assertEqual(String("abcdec").index("c"), 2)
        self.assertEqual(String("cabcdec").index("c", start=2, end=5), 3)
        self.assertRaises(ValueError, lambda: String("abcde").index("f"))

    def test_isalnum(self):
        self.assertTrue(String("abcde123").isalnum())
        self.assertFalse(String("abcde!").isalnum())
        self.assertFalse(String("").isalnum())

    def test_isalpha(self):
        self.assertTrue(String("abcde").isalpha())
        self.assertFalse(String("abcde123").isalpha())
        self.assertFalse(String("").isalpha())

    def test_isdecimal(self):
        self.assertTrue(String("012345").isdecimal())
        self.assertFalse(String("1234A").isdecimal())
        self.assertFalse(String("").isdecimal())

    def test_isdigit(self):
        self.assertTrue(String("012345").isdigit())
        self.assertFalse(String("1234A").isdigit())
        self.assertFalse(String("").isdigit())

    def test_isidentifier(self):
        self.assertFalse(String("012345").isidentifier())
        self.assertTrue(String("A123").isidentifier())
        self.assertFalse(String("$").isidentifier())

    def test_islower(self):
        self.assertTrue(String("abcde").islower())
        self.assertFalse(String("Abcde").islower())
        self.assertFalse(String("").islower())

    def test_isnumeric(self):
        self.assertTrue(String("012345").isdigit())
        self.assertFalse(String("1234A").isdigit())
        self.assertFalse(String("").isdigit())

    def test_isprintable(self):
        self.assertTrue(String("012345").isprintable())
        self.assertTrue(String("").isprintable())

    def test_isspace(self):
        self.assertTrue(String("     ").isspace())
        self.assertFalse(String("  a").isspace())
        self.assertFalse(String("").isspace())

    def test_istitle(self):
        self.assertTrue(String("Abcde").istitle())
        self.assertTrue(String("Ab Cde").istitle())
        self.assertFalse(String("abcDe").istitle())
        self.assertFalse(String("").istitle())

    def test_isupper(self):
        self.assertTrue(String("ABCDE").isupper())
        self.assertFalse(String("Abcde").isupper())
        self.assertFalse(String("").isupper())

    def test_ljust(self):
        self.assertEqual(String("abcde").ljust(3, " "), "abcde")
        self.assertEqual(String("ABCDE").ljust(0, "-"), "ABCDE")
        self.assertEqual(String("Abcde").ljust(10, "-"), "Abcde-----")
        self.assertEqual(String(" ").ljust(9, "-"), " --------")
        self.assertEqual(String("").ljust(10, " "), "          ")

    def test_lower(self):
        self.assertEqual(String("abcde").lower(), "abcde")
        self.assertEqual(String("ABCDE").lower(), "abcde")
        self.assertEqual(String("Ab cde").lower(), "ab cde")
        self.assertEqual(String(" ").lower(), " ")
        self.assertEqual(String("").lower(), "")

    def test_lstrip(self):
        self.assertEqual(String("   spacious   ").lstrip(), "spacious   ")
        self.assertEqual(String("AABAA").lstrip(String("A")), "BAA")
        self.assertEqual(String("ABBA").lstrip("AB"), "")
        self.assertEqual(String("ABCABBA").lstrip("AB"), "CABBA")

    #todo: implement partition and create test
    def test_partition(self):
        pass

    def test_replace(self):
        self.assertEqual(String("abcde").replace("a","b"), "bbcde")
        self.assertEqual(String("ABABE").replace("AB","BB"), "BBBBE")
        self.assertEqual(String("ABABE").replace("AB", "BB", count=1), "BBABE")
        self.assertEqual(String("Ab cde").replace("a","b"), "Ab cde")
        self.assertEqual(String("").replace("",""), "")

    def test_rindex(self):
        self.assertEqual(String("abcde").rindex("a"), 0)
        self.assertEqual(String("abcdec").rindex("c"), 5)
        self.assertEqual(String("cabcdec").rindex("c", start=2, end=5), 3)
        self.assertRaises(ValueError, lambda: String("abcde").rindex("f"))

    def test_rfind(self):
        self.assertEqual(String("abcde").rfind("a"), 0)
        self.assertEqual(String("abcdec").rfind("c"), 5)
        self.assertEqual(String("cabcdec").rfind("c", start=2, end=5), 3)
        self.assertEqual(String("abcde").rfind("f"), -1)

    def test_rjust(self):
        self.assertEqual(String("abcde").rjust(3, " "), "abcde")
        self.assertEqual(String("ABCDE").rjust(0, "-"), "ABCDE")
        self.assertEqual(String("Abcde").rjust(10, "-"), "-----Abcde")
        self.assertEqual(String(" ").rjust(9, "-"), "-------- ")
        self.assertEqual(String("").rjust(10, " "), "          ")

    def test_rstrip(self):
        self.assertEqual(String("   spacious   ").rstrip(), "   spacious")
        self.assertEqual(String("AABAA").rstrip("A"), "AAB")
        self.assertEqual(String("ABBA").rstrip("AB"), "")
        self.assertEqual(String("ABCABBA").rstrip("AB"), "ABC")

    # todo: implement rpartition and create test
    def test_rpartition(self):
        pass

    def test_split(self):
        self.assertEqual(String("a b c").split(), [String("a"), String("b"), String("c")]) #split on space by default
        self.assertEqual(String("a b c").split(" ", 1), [String("a"), String("b c")])
        self.assertEqual(String("a_b_c_d").split("_", 2), [String("a"), String("b"), String("c_d")])
        self.assertEqual(String("").split(), [])

    def test_rsplit(self):
        self.assertEqual(String("a b c").rsplit(), [String("a"), String("b"), String("c")]) #split on space by default
        self.assertEqual(String("a b c").rsplit(" ", 1), [String("a b"), String("c")])
        self.assertEqual(String("a_b_c_d").rsplit("_", 2), [String("a_b"), String("c"), String("d")])
        self.assertEqual(String("").rsplit(), [])

    #todo: doesn't work because Chars only accept certain characters, and \n isnt one of them.
    def test_splitlines(self):
        #self.assertEqual(String("AB\nCD\n").splitlines(), [String("AB"), String("CD")])  # split on space by default
        #self.assertEqual(String("AB\nCD\n").splitlines(True), [String("AB\n"), String("CD\n")])
        #self.assertEqual(String("a_b_c_d").rsplit("_", 2), [String("a_b"), String("c"), String("d")])
        #self.assertEqual(String("").rsplit(), [])
        pass

    def test_strip(self):
        self.assertEqual(String("   spacious   ").strip(), "spacious")
        self.assertEqual(String("AABAA").strip("A"), "B")
        self.assertEqual(String("ABBA").strip("AB"), "")
        self.assertEqual(String("ABCABBA").strip("AB"), "C")

    def test_swapcase(self):
        self.assertEqual(String("abcde").swapcase(), "ABCDE")
        self.assertEqual(String("ABCDE").swapcase(), "abcde")
        self.assertEqual(String("Ab cde").swapcase(), "aB CDE")
        self.assertEqual(String(" ").swapcase(), " ")
        self.assertEqual(String("").swapcase(), "")

    def test_title(self):
        self.assertEqual(String("abcde").title(), "Abcde")
        self.assertEqual(String("ABCDE").title(), "Abcde")
        self.assertEqual(String("Ab cde").title(), "Ab Cde")
        self.assertEqual(String(" ").title(), " ")
        self.assertEqual(String("").title(), "")

    def test_upper(self):
        self.assertEqual(String("abcde").upper(), "ABCDE")
        self.assertEqual(String("ABCDE").upper(), "ABCDE")
        self.assertEqual(String("Ab cde").upper(), "AB CDE")
        self.assertEqual(String(" ").upper(), " ")
        self.assertEqual(String("").upper(), "")

    def test_zfill(self):
        self.assertEqual(String("abcde").zfill(3), "abcde")
        self.assertEqual(String("ABCDE").zfill(0), "ABCDE")
        self.assertEqual(String("Abcde").zfill(10), "00000Abcde")
        self.assertEqual(String(" ").zfill(9), "00000000 ")
        self.assertEqual(String("").zfill(10), "0000000000")

    def test__getitem__(self):
        self.assertEqual(String("abcde").__getitem__(0), "a")
        self.assertEqual(String("abcde")[1], "b")
        self.assertRaises(IndexError, lambda: String("abcde")[6])
        self.assertRaises(IndexError, lambda: String("abcde").__getitem__(6))

    def test__add__(self):
        self.assertEqual(String("a") + String("b"), String("ab"), "__add__: adding String() to String()")
        self.assertEqual(String("a") + "b", String("ab"), "__add__: adding String() to str")

    def test__radd__(self):
        self.assertEqual("a" + String("b"), String("ab"), "__radd__: adding String() to String()")

    def test__mul__(self):
        self.assertEqual(String("a") * Integer(2), String("aa"), "__mul__: adding String() to String()")
        self.assertEqual(String("a") * 2, String("aa"), "__mul__: adding String() to str")

    def test__rmul__(self):
        self.assertEqual(Integer(2) * String("a"), String("aa"), "__rmul__: adding String() to String()")
        self.assertEqual(2 * String("a"), String("aa"), "__rmul__: adding String() to String()")

    #todo: figure out what string mod is supposed to do.
    def test__mod__(self):
        pass

    def test__iter__(self):
        a = iter(String("abc"))
        self.assertEqual(next(a), String("a"))
        self.assertEqual(next(a), String("b"))
        self.assertEqual(next(a), String("c"))
        self.assertRaises(StopIteration, lambda: next(a))

    def test__reversed__(self):
        self.assertEqual(reversed(String("abc")), String("cba"))
        self.assertEqual(reversed(String("aba")), String("aba"))
        self.assertEqual(reversed(String("")), String(""))


if __name__ == '__main__':
    unittest.main()
