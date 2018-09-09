from random import random, randint
from math import trunc, floor, ceil
from Float import Float
from Boolean import Boolean

#mutates roughly by 1 on average
#TODO: not super happy with these, they don't decay far enough from their starting value fast enough, but I can't multiply by their own value because then all ints would become stable at 0.
MUTATION_RATE = 10

#A mutating whole number. Represented internally by a integer whose value changes by MUTATION_RATE / 2 on average.
class Integer:

    _val = 0

    def __init__(self, value):
        self._val = int(value)

    #properties only to be used externally because otherwise recursive reference to mutate
    @property
    def val(self):
        temp = self._val #want the original value to show up atleast once before decay
        self.__mutate()
        return int(temp)

    #properties only to be used externally because otherwise recursive reference to mutate
    @val.setter
    def val(self, value):
        self._val = int(value)

    #mutates the value of this variable
    def __mutate(self):
        #random number between 0 and 1 is scaled down by the mutation rate.
        #Ints would be stable at 0 because 0*anything is 0. This way there is no stable value to decay to.
        mutate_val = randint(0, MUTATION_RATE)
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val) #randomly add or subtract

    # uncomment these after testing
    def __str__(self):
        return int(self.val).__str__()

    def __repr__(self):
        return int(self.val).__repr__()

    #overrides for math ops
    #Todo: Test the math ops

    def __eq__(self, other):
        return Boolean(self.val == other.val)  # self._val == other._val which is better? One has the side effect of mutating the values. Everytime you use a value it should change, that's the assumption of the language.

    def __ne__(self, other):
        return Boolean(self.val != other.val)

    def __lt__(self, other):
        return Boolean(self.val < other.val)

    def __gt__(self, other):
        return Boolean(self.val > other.val)

    def __le__(self, other):
        return Boolean(self.val <= other.val)

    def __ge__(self, other):
        return Boolean(self.val >= other.val)

    def __add__(self, other):
        return Integer(self.val + other.val)

    def __sub__(self, other):
        return Integer(self.val - other.val)

    def __mul__(self, other):
        return Integer(self.val * other.val)

    def __truediv__(self, other):
        return Float(self.val / other.val)

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
        self._val - other.val
        return self

    def __imul__(self, other):
        self._val *= other.val
        return self

    # truediv produces a float, //= does not, following python's int logic.
    #TODO: TEST that this replaces the variable with a float.
    def __itruediv__(self, other):
        return Float(self._val / other.val)

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

    for x in range(10):
        test_dict["a"].append(a)
        test_dict["b"].append(b)
        test_dict["c"].append(c)
        test_dict["d"].append(d)

    for key in test_dict.keys():
        print(key, test_dict[key])

#test()
