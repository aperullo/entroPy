from random import random, randint

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

    #TODO add overrides for comparisons

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
