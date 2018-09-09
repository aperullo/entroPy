from Char import Char

# A convenience class to make using entroPy chars less painful
# Strings shall be immutable.
#TODO: redefine string methods for these.
#TODO: Including getters for selecting by index. String class is fairly useless currently
class String:

    _chars = ()

    def __init__(self, a_string):
        self._chars = tuple(map(Char, a_string)) #For each character in the string, run the Char constructor/create an entropy char out of it

    def __str__(self):
        return "".join(str(c) for c in self._chars)

    def __repr__(self):
        return "".join(str(c) for c in self._chars)

    # def __str__(self):
    #     return self._chars.__str__()
    #
    # def __repr__(self):
    #     return self._chars.__repr__()

    def __len__(self):
        len(self._chars)

    def __eq__(self, other):
        for x in range(max(len(self), len(other))):
           pass


def test():
    a = String("bottles of beer on the wall.")
    for x in range(99):
        print(x,a)

#test()