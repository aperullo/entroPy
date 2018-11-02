import Char
import Integer
from typing import Union, List

# A convenience class to make using entroPy chars less painful
# Strings shall be immutable.
#TODO: Including getters for selecting by index. String class is fairly useless currently
#TODO: typing str or String construct
class String:

    _chars = ()

    def __init__(self, a_string: 'eString'):
        self._chars = tuple(map(Char.Char, a_string)) #For each character in the string, run the Char constructor/create an entropy char out of it

    def __getitem__(self, x):
        return String(self._chars.__getitem__(x))

    # String and printing
    def __str__(self):
        return "".join(str(c) for c in self._chars)

    def __repr__(self):
        return "".join(str(c) for c in self._chars)
        #return "String(_chars="+str(self._chars)+")"

    #calls to len() must return int, can't return Integer.
    def __len__(self) -> int:
        #return Integer(len(self._chars))
        return len(self._chars)


    # Comparison ops.
    def __eq__(self, other: 'eString') -> bool:
        #using str() has the advantage of handling both entropy strings and regular strings.
        return str(self) == str(other)

    def __ne__(self, other: 'eString') -> bool:
        return str(self) != str(other)

    def __lt__(self, other: 'eString') -> bool:
        return str(self) < str(other)

    def __le__(self, other: 'eString') -> bool:
        return str(self) <= str(other)

    def __gt__(self, other: 'eString') -> bool:
        return str(self) > str(other)

    def __ge__(self, other: 'eString') -> bool:
        return str(self) >= str(other)

    def __contains__(self, other: 'eString') -> bool:
        return str(self).__contains__(str(other))


    #todo: make all of these methods return their specific entropy types
    #TODO: test all of these methods
    #TODO: make these methods accept either a String or str as an argument by wrapping the variables in str(other)
    # String specific operations
    # returns string
    def capitalize(self) -> 'String':
        return String(str(self).capitalize())

    # returns string
    def casefold(self) -> 'String':
        return String(str(self).casefold())

    # returns string
    def center(self, width, fillchar) -> 'String':
        return String(str(self).center(width, fillchar))

    # returns int
    def count(self, x: 'eString', start=None, end=None) -> Integer:
        return Integer.Integer(str(self).count(str(x), start, end))

    # return bool
    def endswith(self, suffix: 'eString', start, end) -> bool:
        return str(self).endswith(str(suffix), start, end)

    # returns string
    def expandtabs(self, tabsize=8) -> 'String':
        return String(str(self).expandtabs(tabsize))

    #returns int
    def find(self, sub: 'eString', __start: [int] = ..., __end: [int] = ...):
        return str(self).find(str(sub), __start, __end)

    # returns string
    def format(self, *args, **kwargs) -> 'String':
        return String(str(self).format(*args, **kwargs))

    # def format_map(self, map_obj):
    #     return String(self.__str__().format_map(map_obj))

    #returns int
    def index(self, sub: 'eString', start=None, end=None) -> Integer:
        return Integer.Integer(str(self).index(str(sub), start, end))

    # returns bool
    def isalnum(self) -> bool:
        return str(self).isalnum()

    # returns bool
    def isalpha(self) -> bool:
        return str(self).isalpha()

    # returns bool
    def isdecimal(self) -> bool:
        return str(self).isdecimal()

    # returns bool
    def isdigit(self) -> bool:
        return str(self).isdigit()

    # returns bool
    def isidentifier(self) -> bool:
        return str(self).isidentifier()

    # returns bool
    def islower(self) -> bool:
        return str(self).islower()

    # returns bool
    def isnumeric(self) -> bool:
        return str(self).isnumeric()

    # returns bool
    def isprintable(self) -> bool:
        return str(self).isprintable()

    # returns bool
    def isspace(self) -> bool:
        return str(self).isspace()

    # returns bool
    def istitle(self) -> bool:
        return str(self).istitle()

    # returns bool
    def isupper(self) -> bool:
        return str(self).isupper()

    # returns string
    def join(self, iterable) -> 'String':
        return String(str(self).join(iterable))

    # returns string
    def ljust(self, width, fillchar) -> 'String':
        return String(str(self).ljust(width, fillchar))

    # returns string
    def lower(self) -> 'String':
        return String(str(self).lower())

    # returns string
    def lstrip(self, chars: 'eString'=None) -> 'String':
        return String(str(self).lstrip(chars if chars is None else str(chars)))

    # returns a tuple
    # todo: implement this for entropy strings
    def partition(self, sep):
        return str(self).partition(sep)

    # returns string
    def replace(self, old: 'eString', new: 'eString', count=-1) -> 'String':
        return String(str(self).replace(str(old), str(new), count))

    # returns int
    def rfind(self, sub: 'eString', start=None, end=None) -> Integer:
        return Integer.Integer(str(self).rfind(str(sub), start, end))

    # returns int
    def rindex(self, sub: 'eString', start=None, end=None) -> Integer:
        return Integer.Integer(str(self).rindex(str(sub), start, end))

    # returns string
    def rjust(self, width, fillchar) -> 'String':
        return String(str(self).rjust(width, fillchar))

    # returns a tuple
    def rpartition(self, sep) -> 'String':
        return str(self).rpartition(sep)

    # returns a list of string
    def rsplit(self, sep=None, maxsplit=-1) -> List['String']:
        results = str(self).rsplit(sep if sep is None else str(sep), maxsplit)
        for st in results:
            st = String(st)
        return results

    # returns string
    def rstrip(self, chars: 'eString'=None) -> 'String':
        return String(str(self).rstrip(chars if chars is None else str(chars)))

    # returns a list of string
    def split(self, sep: 'eString'=None, maxsplit=-1) -> List['String']:
        results = str(self).split(sep if sep is None else str(sep), maxsplit)
        for st in results:
            st = String(st)
        return results

    # returns a list of string
    def splitlines(self, keepends: bool=False) -> List['String']:
        results = str(self).splitlines(keepends)
        for st in results:
            st = String(st)
        return results

    # returns bool
    def startswith(self, prefix: 'eString', start, end) -> bool:
        return str(self).startswith(prefix, start, end)

    # returns string
    def strip(self, chars: 'eString'=None) -> 'String':
        return String(str(self).strip(chars if chars is None else str(chars)))

    # returns a string
    def swapcase(self) -> 'String':
        return String(str(self).swapcase())

    # returns a string
    def title(self) -> 'String':
        return String(str(self).title())

    # returns a string
    def upper(self) -> 'String':
        return String(str(self).upper())

    # returns a string
    def zfill(self, width) -> 'String':
        return String(str(self).zfill(width))

    # returns a string
    def __getitem__(self, i) -> 'String':
        return String(str(self).__getitem__(i))

    # returns a string
    def __add__(self, other: 'eString') -> 'String':
        return String(str(self) + str(other))  # str(s) will get the __str__ representation of an entropy String or do nothing if its a primitive str already.

    def __radd__(self, other: 'eString') -> 'String':
        return String(str(other) + str(self))

    # returns a string
    #todo n can be int or Integer
    def __mul__(self, n: int) -> 'String':
        return String(str(self) * int(n))

    # returns a string
    def __rmul__(self, other: int) -> 'String':
        return String(int(other) * str(self))

    # returns a string
    def __mod__(self, value) -> 'String':
        return String(str(self).__mod__(value))

    # returns iterator
    def __iter__(self):
        return self._chars.__iter__()

    # returns int
    def __hash__(self):
        return int(str(self).__hash__())

    # returns string
    def __reversed__(self) -> 'String':
        return String(reversed(str(self)))

#A type representing that a method can take either a primitive str or an entropy String
eString = Union[str, String]

def test():
    a = String("bottles of beer on the wall.")
    for x in range(99):
        print(x,a)

#test()
