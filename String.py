import Char
from Integer import Integer


# A convenience class to make using entroPy chars less painful
# Strings shall be immutable.
#TODO: Including getters for selecting by index. String class is fairly useless currently
class String():

    _chars = ()

    def __init__(self, a_string):
        self._chars = tuple(map(Char.Char, a_string)) #For each character in the string, run the Char constructor/create an entropy char out of it

    def __getitem__(self, x):
        return String(self._chars.__getitem__(x))

    # String and printing
    def __str__(self):
        return "".join(str(c) for c in self._chars)

    def __repr__(self):
        return "".join(str(c) for c in self._chars)

    def __len__(self):
        return Integer(len(self._chars))


    # Comparison ops.
    def __eq__(self, other):
        #using str() has the advantage of handling both entropy strings and regular strings.
        return str(self) == str(other)


    #todo: make all of these methods return their specific entropy types
    #TODO: test all of these methods
    #TODO: make these methods accept either a String or str as an argument by wrapping the variables in str(other)
    # String specific operations
    # returns string
    def capitalize(self):
        return String(str(self).capitalize())

    # returns string
    def casefold(self):
        return String(str(self).casefold())

    # returns string
    def center(self, width, fillchar):
        return String(str(self).center(width, fillchar))

    # returns int
    def count(self, x, __start, __end):
        return String(str(self).count(x, __start, __end))

    # return boolean
    def endswith(self, suffix, start, end):
        return str(self).endswith(suffix, start, end)

    # returns string
    def expandtabs(self, tabsize: int = 8):
        return String(str(self).expandtabs(tabsize))

    #returns int
    def find(self, sub: str, __start: [int] = ..., __end: [int] = ...):
        return str(self).find(sub, __start, __end)

    # returns string
    def format(self, *args, **kwargs):
        return String(str(self).format(*args, **kwargs))

    # def format_map(self, map_obj):
    #     return String(self.__str__().format_map(map_obj))

    #returns int
    def index(self, sub: str, __start, __end):
        return Integer(str(self).index(sub, __start, __end))

    # returns bool
    def isalnum(self):
        return str(self).isalnum()

    # returns bool
    def isalpha(self):
        return str(self).isalpha()

    # returns bool
    def isdecimal(self):
        return str(self).isdecimal()

    # returns bool
    def isdigit(self):
        return str(self).isdigit()

    # returns bool
    def isidentifier(self):
        return str(self).isidentifier()

    # returns bool
    def islower(self):
        return str(self).islower()

    # returns bool
    def isnumeric(self):
        return str(self).isnumeric()

    # returns bool
    def isprintable(self):
        return str(self).isprintable()

    # returns bool
    def isspace(self):
        return str(self).isspace()

    # returns bool
    def istitle(self):
        return str(self).istitle()

    # returns bool
    def isupper(self):
        return str(self).isupper()

    # returns string
    def join(self, iterable):
        return String(str(self).join(iterable))

    # returns string
    def ljust(self, width, fillchar):
        return String(str(self).ljust(width, fillchar))

    # returns string
    def lower(self):
        return String(str(self).lower())

    # returns string
    def lstrip(self, chars):
        return String(str(self).lstrip(chars))

    # returns a tuple
    # todo: implement this for entropy strings
    def partition(self, sep):
        return str(self).partition(sep)

    # returns string
    def replace(self, old, new, count):
        return String(str(self).replace(old, new, count))

    # returns int
    def rfind(self, sub, __start, __end):
        return Integer(str(self).rfind(sub, __start, __end))

    # returns int
    def rindex(self, sub, __start, __end):
        return Integer(str(self).rindex(sub, __start, __end))

    # returns string
    def rjust(self, width, fillchar):
        return String(str(self).rjust(width, fillchar))

    # returns a tuple
    def rpartition(self, sep):
        return str(self).rpartition(sep)

    # returns a list of string
    def rsplit(self, sep, maxsplit):
        results = str(self).rsplit(sep, maxsplit)
        for st in results:
            st = String(st)
        return results

    # returns string
    def rstrip(self, chars):
        return String(str(self).rstrip(chars))

    # returns a list of string
    def split(self, sep, maxsplit):
        results = str(self).split(sep, maxsplit)
        for st in results:
            st = String(st)
        return results

    # returns a list of string
    def splitlines(self, keepends):
        results = str(self).splitlines(keepends)
        for st in results:
            st = String(st)
        return results

    # returns bool
    def startswith(self, prefix, start, end):
        return str(self).startswith(prefix, start, end)

    # returns string
    def strip(self, chars):
        return String(str(self).strip(chars))

    # returns a string
    def swapcase(self):
        return String(str(self).swapcase())

    # returns a string
    def title(self):
        return String(str(self).title())

    # returns a string
    def upper(self):
        return String(str(self).upper())

    # returns a string
    def zfill(self, width: int):
        return String(str(self).zfill(width))

    # returns a string
    def __getitem__(self, i):
        return String(str(self).__getitem__(i))

    # returns a string
    def __add__(self, s):
        return String(str(self).__add__(str(s)))  # str(s) will get the __str__ representation of an entropy String or do nothing if its a primitive str already.

    # returns a string
    def __mul__(self, n: int):
        return String(str(self).__mul__(n))

    # returns a string
    def __rmul__(self, n: int):
        return String(str(self).__rmul__(n))

    # returns a string
    def __mod__(self, value):
        return String(str(self).__mod__(value))

    # returns bool
    def __ne__(self, x: object):
        return str(self).__ne__(x)

    # returns bool
    def __lt__(self, x: str):
        return str(self).__lt__(x)

    # returns bool
    def __le__(self, x: str):
        return str(self).__le__(x)

    # returns bool
    def __gt__(self, x: str):
        return str(self).__gt__(x)

    # returns bool
    def __ge__(self, x: str):
        return str(self).__ge__(x)

    # returns bool
    def __contains__(self, s):
        return str(self).__contains__(s)

    # returns iterator
    def __iter__(self):
        temp = self._chars.__iter__()
        return self._chars.__iter__()

    # returns int
    def __hash__(self):
        return Integer(str(self).__hash__())

    # returns string
    def __reversed__(self):
        return String(str(self).__reversed__())


def test():
    a = String("bottles of beer on the wall.")
    for x in range(99):
        print(x,a)

#test()
