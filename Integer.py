from random import random, randint, uniform
from math import trunc, floor, ceil
import Float, String
import Settings


#MUTATION_RATE = Settings.get_mutation_rate("Integer")

#A mutating whole number. Represented internally by a float whose value get rounded off.
class Integer:

    _val = 0.0

    def __init__(self, value):
        self._val = round(value, 0) #round the incoming number to 0 decimal palces.

    @property
    def val(self):
        temp = self._val # want the original value to show up atleast once before decay
        self.__mutate()
        return int(temp)

    @val.setter
    def val(self, value):
        self._val = float(round(value, 0)) #val always needs to be a float.

    # mutates the value of this variable
    def __mutate(self):
        # Random number between 1 and MUTATION_RATE * the magnitude of the value itself.
        # If Mutation rate is 1 then there is stability at 1 and all numbers will hover around 1 on average, but may fluctuate to higher values.
        # If Mutation rate is higher (ie 2), then numbers change by twice their value on average leading to exponential fluctuations.
        # It can still settle at 1 or 0, but it is much easier for it to escape from that stable place.
        # This finally achieves the behavior I want.

        MUTATION_RATE = Settings.get_mutation_rate("Integer")
        mutate_val = uniform(1.0, abs(self._val) if abs(self._val) >= 1 else 1.0)  #multiply by the magnitude of the value or atleast by 1.
        mutate_val *= MUTATION_RATE
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val)  # randomly add or subtract


    # String and printing
    def __str__(self) -> str:
        return int(self.val).__str__()

    def __repr__(self) -> str:
        # return int(self.val).__str__()
        return "Integer(_val=" + self._val.__repr__() + ")"


    # These methods allow entropy types to imitate their primitive counterparts in most situations.
    # Some functions will try running the int or index function on an object to see if it can be duck typed to acting as an int.
    def __index__(self) -> int:
        return int(self.val)

    def __int__(self) -> int:
        return int(self.val)

    def __float__(self) -> float:
        return float(round(self.val, 0)) #val always needs to be a float.

    # Comparison ops. These used to return entropy booleans but that ended up causing while loops to just simply stop with no visible explanation.
    # For the sake of making the language usable, entropy booleans will probably end up confined to only user made booleans, or just be removed entirely.
    def __eq__(self, other) -> bool:
        return self.val == float(other)

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
        return Integer(self.val + float(other))

    def __radd__(self, other):
        return Integer(self.val + float(other))

    def __iadd__(self, other):
        self._val += float(other)
        self.__mutate()
        return self

    def __sub__(self, other):
        return Integer(self.val - float(other))

    def __rsub__(self, other):
        return Integer(float(other) - self.val)

    def __isub__(self, other):
        self._val -= float(other)
        self.__mutate()
        return self

    def __mul__(self, other):
        if isinstance(other, String.String):
            return NotImplemented  # deals with Integer * String by passing priority to String's rmul.
        return Integer(self.val * float(other))

    def __rmul__(self, other):
        return Integer(self.val * float(other))

    def __imul__(self, other):
        self._val *= float(other)
        self.__mutate()
        return self

    def __truediv__(self, other):
        return Float.Float(self.val / float(other))

    def __rtruediv__(self, other):
        return Float.Float(float(other) / self.val)

    def __itruediv__(self, other):
        self.__mutate()
        return Float.Float(self._val / float(other))

    def __floordiv__(self, other):
        return Integer(self.val // float(other))

    def __rfloordiv__(self, other):
        return Integer(float(other) // self.val)

    # truediv produces a float, //= does not, following python's int logic.
    def __ifloordiv__(self, other):
        self._val //= float(other)
        self.__mutate()
        return self

    def __mod__(self, other):
        return Integer(self.val % float(other))

    def __rmod__(self, other):
        return Integer(float(other) % self.val)

    def __imod__(self, other):
        self._val %= float(other)
        self.__mutate()
        return self

    def __divmod__(self, other):
        return "NOT IMPLEMENTED YET"
        #return Integer(divmod(self.val, float(other)))

    def __divmod__(self, other):
        return tuple(map(Integer, divmod(self.val, float(other)))) # for both of the things in the tuple, run the float constructor over them.

    def __rdivmod__(self, other):
        return tuple(map(Integer, divmod(float(other), self.val))) # for both of the things in the tuple, run the float constructor over them.

    def __pow__(self, other):
        return Integer(pow(self.val, float(other)))

    def __rpow__(self, other):
        return Integer(pow(float(other), self.val))

    def __ipow__(self, other):
        self._val = pow(self._val, float(other))
        self.__mutate()
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

    def __hash__(self):
        return int(hash(self.val))


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
