import unittest
from Float import Float
from Integer import Integer
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

if __name__ == '__main__':
    unittest.main()

#Float tests