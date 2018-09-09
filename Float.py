from random import random

MUTATION_RATE = 0.05

#A mutating floating point number.
class Float:

    _val = 0.0

    def __init__(self, value):
        self._val = value

    #properties only to be used externally because otherwise recursive reference to mutate
    @property
    def val(self):
        temp = self._val
        self.__mutate()
        return temp

    #properties only to be used externally because otherwise recursive reference to mutate
    @val.setter
    def val(self, value):
        self._val = value

    #mutates the value of this variable
    def __mutate(self):
        #random number between 0 and 1 is scaled down by the mutation rate and then scaled again by the value itself
        mutate_val = self._val * MUTATION_RATE * random()
        self._val = self._val + (mutate_val if random() < 0.5 else -mutate_val) #randomly add or subtract

    # uncomment these after testing
    def __str__(self):
        return self.val.__str__()

    def __repr__(self):
        return self.val.__repr__()

    #TODO add overrides for math ops

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

test()
