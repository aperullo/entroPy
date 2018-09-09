from random import random
from Integer import Integer
from Float import Float

MUTATION_RATE = 0.5 #50/50 odds of being false or true

#A mutating true/false.
#TODO: currently only supports a subset of the ascii character set. 32-126 or " " to "~".
#TODO: In the future instead of clamping so values can get stuck after they decay to either side, maybe use a modulo type operation to connect the lower and upper bound in a loop
class Boolean:

    _val = False

    def __init__(self, value):
        #try to use value like a char is pythonic, hopefully its not a number representing the ascii value or that number as a string.
        self._val = value

    #properties only to be used externally because otherwise recursive reference to mutate
    @property
    def val(self):
        temp = self._val #want the original value to show up atleast once before decay
        self.__mutate()
        return self._val

    #properties only to be used externally because otherwise recursive reference to mutate
    @val.setter
    def val(self, value):
        self._val = value

    #mutates the value of this variable
    def __mutate(self):
        self._val = random() < MUTATION_RATE #randomly be true or false

    # uncomment these after testing
    def __str__(self):
        return self.val.__str__()

    def __repr__(self):
        return self.val.__repr__()

    #overrides for comparisons

    #determines truthiness of a class
    #I know the == True is redundant, but it might make the ifuncs behave if self._val ends up becoming an integer instead
    def __bool__(self):
        return self.val == True

    def __eq__(self, other):
        return Boolean(self.val == other.val)

    def __ne__(self, other):
        return Boolean(self.val != other.val)

    def __lshift__(self, other):
        return Integer(self.val << other.val)

    def __rshift__(self, other):
        return Integer(self.val >> other.val)

    def __and__(self, other):
        return Boolean(self.val & other.val)

    def __xor__(self, other):
        return Boolean(self.val ^ other.val)

    def __or__(self, other):
        return Boolean(self.val | other.val)

    def __ilshift__(self, other):
        return Integer(self.val << other.val)

    def __irshift__(self, other):
        return Integer(self.val >> other.val)

    def __iand__(self, other):
        return Boolean(self.val & other.val)

    def __ixor__(self, other):
        return Boolean(self.val ^ other.val)

    def __ior__(self, other):
        return Boolean(self.val | other.val)

    #You can do math with booleans because they are just 0 and 1, so we need to implement that math methods too.

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

    # TODO: TEST that this replaces the variables with an Integer.
    def __iadd__(self, other):
        return Integer(self._val + other.val)

    def __isub__(self, other):
        return Integer(self._val - other.val)

    def __imul__(self, other):
        return Integer(self._val * other.val)

    # truediv produces a float, //= does not, following python's int logic.
    def __itruediv__(self, other):
        return Float(self._val / other.val)

    def __ifloordiv__(self, other):
        return Integer(self._val // other.val)

    def __imod__(self, other):
        return Integer(self._val % other.val)

    def __ipow__(self, other):
        return Integer(pow(self._val,other.val))

def test():
    a = Boolean(False)
    true, false = 0, 0
    for x in range(1000):
        if a:
            true += 1
        else:
            false += 1

    print(true, false)

#test()
