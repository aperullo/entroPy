from random import random

MUTATION_RATE = 0.004
LOWER_BOUND = 32 #" " in ascii
UPPER_BOUND = 126 #"~" in ascii

#A mutating single character. Represented internally by a float whose value gets rounded off when read.
#TODO: currently only supports a subset of the ascii character set. 32-126 or " " to "~".
#TODO: In the future instead of clamping so values can get stuck after they decay to either side, maybe use a modulo type operation to connect the lower and upper bound in a loop
class Char:

    _val = int(((UPPER_BOUND - LOWER_BOUND) / 2) + LOWER_BOUND)  #gets the middle of the limited ascii range allowed, allowing it mutate up or down.

    def __init__(self, value):
        #try to use value like a char is pythonic, hopefully its not a number representing the ascii value or that number as a string.
        self._val = self.__validate(ord(value))

    #makes sure that the value stays within our limited ascii range
    #there are plenty of fancy ways to write clamp functions but this is the most readable;
    def __validate(self, value):
        if value < LOWER_BOUND:
            return LOWER_BOUND
        elif value > UPPER_BOUND:
            return UPPER_BOUND
        else:
            return value

    #properties only to be used externally because otherwise recursive reference to mutate
    @property
    def val(self):
        temp = self._val #want the original value to show up atleast once before decay
        self.__mutate()
        return int(round(self.__validate(temp)))

    #properties only to be used externally because otherwise recursive reference to mutate
    @val.setter
    def val(self, value):
        self._val = self.__validate(ord(value))

    #mutates the value of this variable
    def __mutate(self):
        #random number between 0 and 1 is scaled down by the mutation rate and then scaled again by the value itself
        mutate_val = self._val * MUTATION_RATE * random()
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val) #randomly add or subtract

    # uncomment these after testing
    def __str__(self):
        return chr(self.val).__str__()

    def __repr__(self):
        return chr(self.val).__repr__()

    #TODO add overrides for comparisons

def test():
    a = Char("a")
    b = Char("0")
    c = Char(' ')
    d = Char("~")

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
