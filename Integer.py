from random import random, randint, uniform
from math import trunc, floor, ceil
import Float
import Settings


MUTATION_RATE = Settings.get_mutation_rate("Integer")

#A mutating whole number. Represented internally by a integer whose value changes by MUTATION_RATE / 2 on average.
class Integer:

    _val = 0

    def __init__(self, value):
        self._val = int(value)

    @property
    def val(self):
        temp = self._val # want the original value to show up atleast once before decay
        self.__mutate()
        return int(temp)

    @val.setter
    def val(self, value):
        self._val = int(value)

    # mutates the value of this variable
    def __mutate(self):
        # Random number between 1 and MUTATION_RATE * the magnitude of the value itself.
        # If Mutation rate is 1 then there is stability at 1 and all numbers will hover around 1 on average, but may fluctuate to higher values.
        # If Mutation rate is higher (ie 2), then numbers change by twice their value on average leading to exponential fluctuations.
        # It can still settle at 1 or 0, but it is much easier for it to escape from that stable place.
        # This finally achieves the behavior I want.

        mutate_val = uniform(1, MUTATION_RATE * abs(self._val) if abs(self._val) >= 1 else 1)  #multiply by the magnitude of the value or atleast by 1.
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val) #randomly add or subtract


    # String and printing
    def __str__(self):
        return int(self.val).__str__()

    def __repr__(self):
        return int(self.val).__repr__()


    # These methods allow entropy types to imitate their primitive counterparts in most situations.
    # Some functions will try running the int or index function on an object to see if it can be duck typed to acting as an int.
    def __int__(self):
        return int(self.val)

    def __float__(self):
        return self.val

    def __index__(self):
        return int(self.val)


    # Comparison ops. These used to return entropy booleans but that ended up causing while loops to just simply stop with no visible explanation.
    # For the sake of making the language usable, entropy booleans will probably end up confined to only user made booleans, or just be removed entirely.
    def __eq__(self, other):
        return self.val == other.val

    def __ne__(self, other):
        return self.val != other.val

    def __lt__(self, other):
        return self.val < other.val

    def __gt__(self, other):
        return self.val > other.val

    def __le__(self, other):
        return self.val <= other.val

    def __ge__(self, other):
        return self.val >= other.val

    # Math ops overrides. These persist the type by making the result an entropy type.
    # Todo: Test the math ops
    def __add__(self, other):
        return Integer(self.val + other.val)

    def __sub__(self, other):
        return Integer(self.val - other.val)

    def __mul__(self, other):
        return Integer(self.val * other.val)

    def __truediv__(self, other):
        return Float.Float(self.val / other.val)

    def __floordiv__(self, other):
        return Integer(self.val // other.val)

    def __mod__(self, other):
        return Integer(self.val % other.val)

    def __divmod__(self, other):
        return Integer(divmod(self.val, other.val))

    def __pow__(self, other):
        return Integer(pow(self.val, other.val))

    def __iadd__(self, other):
        self._val += other.val
        return self

    def __isub__(self, other):
        self._val -= other.val
        return self

    def __imul__(self, other):
        self._val *= other.val
        return self

    # truediv produces a float, //= does not, following python's int logic.
    #TODO: TEST that this replaces the variable with a float.
    def __itruediv__(self, other):
        return Float.Float(self._val / other.val)

    def __ifloordiv__(self, other):
        self._val //= other.val
        return self

    def __imod__(self, other):
        self._val %= other.val
        return self

    def __ipow__(self, other):
        self._val = pow(self._val,other.val)
        return self

    def __neg__(self):
        return Integer(-self.val)

    def __pos__(self):
        return Integer(+self.val)

    def __abs__(self):
        return Integer(abs(self.val))

    def __invert__(self):
        return Integer(~self.val)

    def __round__(self, n=None):
        return Integer(round(self.val, n))

    def __trunc__(self):
        return Integer(trunc(self.val))

    def __floor__(self):
        return Integer(floor(self.val))

    def __ceil__(self):
        return Integer(ceil(self.val))


def test():
    a = Integer(1)
    b = Integer(0)
    c = Integer(-1)
    d = Integer(255)

    test_dict = {
        "a": [a],
        "b": [b],
        "c": [c],
        "d": [d]
    }

    for x in range(50):
        test_dict["a"].append(a)
        test_dict["b"].append(b)
        test_dict["c"].append(c)
        test_dict["d"].append(d)

    for key in test_dict.keys():
        print(key, test_dict[key])

#test()
