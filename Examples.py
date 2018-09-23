"""
A file of example functions for seeing entropy in action.

The functions aren't written to be the most efficient of their kind, but to test various common and uncommon uses of the types.
"""


def interweave(string1, string2):
    """
    A function that interweaves two strings letter by letter.

    Args:
        string1 (str): First string to interweave
        string2 (str): Second string to interweave

    Returns:
        str: The resulting string

    Entropy Behavior:
        May sometimes return an incomplete interweaved string, or even no string at all. This happens when the len values drift
        to shorter than the actual string or even to 0.

        Also demonstrates that len, which explicity returns an int rather than an Integer, becomes implicitly wrapped in
        an Integer() call to allow lengths to drift.

        Taking advantage of the fact that entropy values don't change on their initial read and that entropy strings
        support iteration, we are able to keep the values of the string from drifting.
    """
    # make some iterators to get the next letters
    itr1, itr2 = iter(string1), iter(string2)
    result = ""

    # repeat until we've done every letter in the string
    for x in range(max(len(string1), len(string2))):

        char1 = next(itr1, "")  # get the next letter or return an empty string if the iterator is exhausted.
        char2 = next(itr2, "")

        result += char1+char2

    return result


def bottles(bottles=99):
    """
    Prints the children's rhyme 99 bottles.

    Args:
        bottles (int/float): The number of bottles to count off. Default 99. (optional)

    Entropy Behavior:
        Visually demonstrates how Integers/Floats and Strings decay every time they are read.

        Using an Integer can cause only a few verses to be printed because they can fluctuate so wildly at the default value.
        Changing INTEGER_MUTATION_RATE to 0.1 is a good value for this demo.

        Using a Float generally produces a more traditional number of verses but has the side effect of having many decimal places following the number.
        IE 99.24964258401461 bottles of beer on the wall.
    """
    sentence = "bottles of beer on the wall."

    # rather than while bottles > 0 we do bottles is greater than 1.0.
    # This lets the function handle entropy Integers and Floats just as well, since floats may decay arbitrarily close to 0 without ever going negative.
    while bottles > 1.0:
        print(bottles, sentence)
        bottles -= 1.0


"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""