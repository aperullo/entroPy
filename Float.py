from random import random
from math import trunc, floor, ceil
import Integer
import Settings

#A mutating floating point number.
class Float:

    _val = 0.0

    def __init__(self, value):
        self._val = value

    @property
    def val(self):
        temp = self._val
        self.__mutate()
        return temp

    @val.setter
    def val(self, value):
        self._val = float(value)

    # mutates the value of this variable
    def __mutate(self):
        MUTATION_RATE = Settings.get_mutation_rate("Float") # calling this everytime every variable mutates seems like it could be very slow.
                                                            # But this is a way to ensure the settings can be modified while the program is running.
        # random number between 0 and 1 is scaled down by the mutation rate and then scaled again by the value itself
        mutate_val = self._val * MUTATION_RATE * random()
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val) #randomly add or subtract


    # String and printing
    def __str__(self) -> str:
        return self.val.__str__()

    #Should repr alter the value? Since repr is meant for debugging probably not.
    #but if something used it instead of str() then floats wont mutate as expected.
    def __repr__(self) -> str:
        # return self.val.__str__()
        return "Float(_val=" + self._val.__repr__() + ")"


    # These methods allow entropy types to imitate their primitive counterparts in most situations.
    # Some functions will try running the int or index function on an object to see if it can be duck typed to acting as an int.
    def __index__(self) -> int:
        return int(self.val)

    def __int__(self) -> int:
        return int(self.val)

    def __float__(self) -> float:
        return float(self.val)

    # Comparison ops. These used to return entropy booleans but that ended up causing while loops to just simply stop with no visible explanation.
    # For the sake of making the language usable, entropy booleans will probably end up confined to only user made booleans, or just be removed entirely.
    def __eq__(self, other) -> bool:
        return self.val == float(other)    #call self.val. Everytime you use a value it should change, that's the assumption of the language.

    def __ne__(self, other) -> bool:
        return self.val != float(other)

    def __lt__(self, other) -> bool:
        return self.val < float(other)

    def __gt__(self, other) -> bool:
        return self.val > float(other)

    def __le__(self, other) -> bool:
        return self.val <= float(other)

    def __ge__(self, other) -> bool:
        return self.val >= float(other)


    # Math ops overrides. These persist the type by making the result an entropy type.
    def __add__(self, other):
        return Float(self.val + float(other))

    def __radd__(self, other):
        return Float(self.val + float(other))

    def __iadd__(self, other):
        self._val += float(other)
        self.__mutate()
        return self

    def __sub__(self, other):
        return Float(self.val - float(other))

    def __rsub__(self, other):
        return Float(float(other) - self.val)

    def __isub__(self, other):
        self._val -= float(other)
        self.__mutate()
        return self

    def __mul__(self, other):
        return Float(self.val * float(other))

    def __rmul__(self, other):
        return Float(self.val * float(other))

    def __imul__(self, other):
        self._val *= float(other)
        self.__mutate()
        return self

    def __truediv__(self, other):
        return Float(self.val / float(other))

    def __rtruediv__(self, other):
        return Float(float(other) / self.val)

    def __itruediv__(self, other):
        self._val /= float(other)
        self.__mutate()
        return self

    def __floordiv__(self, other):
        return Float(int(self.val // float(other))) # int() to truncate

    def __rfloordiv__(self, other):
        return Float(int(float(other) // self.val)) # int() to truncate

    # floordiv produces an integer, //= does not, following python's float logic.
    def __ifloordiv__(self, other):
        self._val //= float(other)
        self.__mutate()
        return self

    def __mod__(self, other):
        return Float(self.val % float(other))

    def __rmod__(self, other):
        return Float(float(other) % self.val)

    def __imod__(self, other):
        self._val %= float(other)
        self.__mutate()
        return self

    def __divmod__(self, other):
        return tuple(map(Float, divmod(self.val, float(other)))) # for both of the things in the tuple, run the float constructor over them.

    def __rdivmod__(self, other):
        return tuple(map(Float, divmod(float(other), self.val))) # for both of the things in the tuple, run the float constructor over them.

    def __pow__(self, other):
        return Float(pow(self.val, float(other)))

    def __rpow__(self, other):
        return Float(pow(float(other), self.val))

    def __ipow__(self, other):
        self._val = pow(self._val,float(other))
        self.__mutate()
        return self

    def __neg__(self):
        return Float(-self.val)

    def __pos__(self):
        return Float(+self.val)

    def __abs__(self):
        return Float(abs(self.val))

    def __round__(self, n=None):
        return Float(round(self.val, n))

    def __trunc__(self):
        return Integer.Integer(trunc(self.val))


def test():
    a = Float(1.0)
    b = Float(1)
    c = Float(-1)
    d = Float(100)
    test_dict = {
        "a": [a],
        "b": [b],
        "c": [c],
        "d": [d]
    }

    for x in range(100):
        test_dict["a"].append(a)
        test_dict["b"].append(b)
        test_dict["c"].append(c)
        test_dict["d"].append(d)

    for key in test_dict.keys():
        print(key, test_dict[key])

#test()
