from random import random
# from Integer import Integer
# from Float import Float
import Integer
import Float
import Settings

MUTATION_RATE = Settings.get_mutation_rate("Boolean")

#A mutating true/false.
#TODO: This class may become deprecated. Makes many programs too unstable.
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
        self._val = (not self._val) if (random() <= MUTATION_RATE) else self._val  #Mutation_rate represents the chance to mutate where 0 is never and 1 is can mutate everytime.


    # uncomment these after testing
    def __str__(self):
        return self.val.__str__()

    def __repr__(self):
        return self.val.__repr__()

    # This method allow the entropy type to imitate its primitive counterpart in most situations.
    # Some functions will try running the bool function to determine the objects "truthiness".
    def __bool__(self):
        # I know the == True is redundant, but it might make the ifuncs behave if self._val ends up becoming an integer instead
        return self.val == True


    # Comparison ops. These used to return entropy booleans but that ended up causing while loops to just simply stop with no visible explanation.
    # For the sake of making the language usable, entropy booleans will probably end up confined to only user made booleans, or just be removed entirely.
    def __eq__(self, other):
        return self.__bool__() == other.__bool__()

    def __ne__(self, other):
        return self.__bool__() != other.__bool__()

    def __lshift__(self, other):
        return Integer.Integer(self.val << other.val)

    def __rshift__(self, other):
        return Integer.Integer(self.val >> other.val)

    def __and__(self, other):
        return self.__bool__() & other.__bool__()

    def __xor__(self, other):
        return self.__bool__() ^ other.__bool__()

    def __or__(self, other):
        return self.__bool__() | other.__bool__()

    def __ilshift__(self, other):
        return Integer.Integer(self.val << other.val)

    def __irshift__(self, other):
        return Integer.Integer(self.val >> other.val)

    def __iand__(self, other):
        self._val = self & other
        return self

    def __ixor__(self, other):
        self._val = self ^ other
        return self

    def __ior__(self, other):
        self._val = self | other
        return self

    #You can do math with booleans because they are just 0 and 1, so we need to implement that math methods too.
    def __add__(self, other):
        return Integer.Integer(self.val + other.val)

    def __sub__(self, other):
        return Integer.Integer(self.val - other.val)

    def __mul__(self, other):
        return Integer.Integer(self.val * other.val)

    def __truediv__(self, other):
        return Float.Float(self.val / other.val)

    def __floordiv__(self, other):
        return Integer.Integer(self.val // other.val)

    def __mod__(self, other):
        return Integer.Integer(self.val % other.val)

    def __divmod__(self, other):
        return Integer.Integer(divmod(self.val, other.val))

    def __pow__(self, other):
        return Integer.Integer(pow(self.val, other.val))

    #todo: should these i methods be allowed to turn the _val into an integer? Probably.
    def __iadd__(self, other):
        return Integer.Integer(self._val + other.val)

    def __isub__(self, other):
        return Integer.Integer(self._val - other.val)

    def __imul__(self, other):
        return Integer.Integer(self._val * other.val)

    # truediv produces a float, //= does not, following python's int logic.
    def __itruediv__(self, other):
        return Float.Float(self._val / other.val)

    def __ifloordiv__(self, other):
        return Integer.Integer(self._val // other.val)

    def __imod__(self, other):
        return Integer.Integer(self._val % other.val)

    def __ipow__(self, other):
        return Integer.Integer(pow(self._val,other.val))


def test():
    a = Boolean(False)
    true, false = 0, 0
    for x in range(100000):
        if a:
            true += 1
        else:
            false += 1

    print(true, false)

#test()
