from Char import Char

# A convenience class to make using entroPy chars less painful
# Strings shall me immutable. TODO: make everything immutable other than by decay? Basically remove setters and make math ops class methods
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