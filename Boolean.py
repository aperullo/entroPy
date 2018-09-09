from random import random
import Integer

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
        return chr(self.val).__str__()

    def __repr__(self):
        return chr(self.val).__repr__()

    #overrides for comparisons

    #determines truthiness of a class

    def __bool__(self):
        return self.val

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
