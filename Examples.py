"""
A file of example functions for seeing entropy in action.

The functions aren't written to be the most efficient of their kind, but to test various common and uncommon uses of the types.
"""
from random import choice
from typing import Dict, Union

def interweave(string1: str, string2: str) -> str:
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


def bottles(bottles: Union[int, float]=99):
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


#to be strong enough, the password must be atleast 6 chars, 1 upper, 1 lower, 1 number, and 1 special.
#If not strong enough return a stronger version of the password.
#if strong enough, just return the password
def pass_suggest(password: str) -> str:
    """
    Checks a password against some pre-coded rules and either returns the original, or a modified suggestion that passes the rules.

    The rules it checks against are: Contains atleast 1 digit, atleast 1 lowercase letter, 1 uppercase letter, and 1 special character

    Args:
        password: the password to check and suggest for.

    Returns:
        Returns the original password string or a modified suggestion that passes the rules.

    Entropy Behavior:
        The returned string may actually end up shorter or longer than required depending on whether the MIN_PASSWORD_LENGTH mutated.
        The returned string may contained altered (rather than only appended) characters compared to the original password.
        A character in the returned string may sometimes mutate to a different alphabet, meaning the returned value won't satisfy the requirements.
    """

    lexicon = {
        "numbers": "0123456789",
        "lower_case": "abcdefghijklmnopqrstuvwxyz",
        "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "special_characters": "!@#$%^&*()-+"
    }
    MIN_PASSWORD_LENGTH = 6

    results = _pass_check(password, lexicon)

    new_password = password
    for req_type, fulfilled in results.items():
        # if the requirement wasn't fulfilled
        if not fulfilled:
            # get the corresponding alphabet and append a random character to the current password. Default to lower_case alphabet in case key not found.
            new_password += choice(lexicon.get(req_type, "abcdefghijklmnopqrstuvwxyz"))

    # We can ignore the length check until after we finish possibly altering the password. It might be the req after
    while len(new_password) < MIN_PASSWORD_LENGTH:
        #add a random character from a random alphabet.
        new_password += choice(lexicon.get(choice(list(lexicon.keys())), "abcdefghijklmnopqrstuvwxyz"))

    return new_password

#helper for two passwd based functions
#checks password against the requirements and returns a dictionary containing whether the requirement was satisfied.
def _pass_check(passwd: str, requirements: Dict[str, str]) -> Dict[str, bool]:
    results = {}

    # for every requirement type and it's alphabet
    for req_type, alphabet in requirements.items():
        # for each letter in password, is that char in the current alphabet?
        letter_map = map(lambda letter: letter in alphabet, passwd)

        # were any of the chars matched?
        results[req_type] = any(letter_map)

    return results


# this function rates the strength of a password using a pre-coded set of rules.
# does not actually correspond to real difficulty in bruteforcing, rules are arbitrary to allow demoing entropy.
def pass_strength(password: str) -> str:
    """
    This function rates the strength of a password using a pre-coded set of rules.

    The rating does not actually correspond to real difficulty in bruteforcing, rules are arbitrary to allow demoing entropy.
    Passwords are rated from 0-15 in strength. The rules are +1 point for having atleast 1 character,
    +1 point for meeting minimum number of chars (+1 more for every two chars over the minimum), +2 for atleast one number,
    +1 for atleast one lower case, +2 for atleast one upper case, and +2 for atleast 1 symbol.

    Args:
        password: A password to rate the strength of.

    Returns:
        a string describing the strength of the password

    Entropy Behavior:
        The point values awarded change from run to run. The max number of points changes to be higher or even lower than should be reasonable.
        Points may become negative. The rating given may not correspond to the number of points. The rating may become none because the actual
        score mutated outside the bounds of the dictionary. The password itself rarely may change, leading to inaccurate "contains" tests.
        The progress bar may contain more or less full and empty marks than the score would indicate.
    """

    lexicon = {
        "numbers": "0123456789",
        "lower_case": "abcdefghijklmnopqrstuvwxyz",
        "upper_case": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "special_characters": "!@#$%^&*()-+"
    }
    MIN_PASSWORD_LENGTH = 6
    MAX_POINTS = 15
    strength_points = 1 if len(password) > 0 else 0

    # how far over the minimum length is the passwd, if at all?
    length_over = len(password) - MIN_PASSWORD_LENGTH
    if length_over >= 0:
        # award 1 point for exceeding the req, +1 more for every 2 chars over. In reality, each additional char leads to an exponential increase in complexity. Not modeled here.
        strength_points += 1 + (max(length_over, 0) // 2)

    # check character usage
    results = _pass_check(password, lexicon)

    if results.get("numbers", False):
        strength_points += 2

    if results.get("lower_case", False):
        strength_points += 1

    if results.get("upper_case", False):
        strength_points += 2

    if results.get("special_characters", False):
        strength_points += 2

    # strength points max will be 15
    strength_points = min(strength_points, MAX_POINTS)

    result_string = ""
    # there are 4 levels of strength so divide point total by 4 to fit it into one of the categories.
    strength = {0:"Weak",
                1:"Average",
                2:"Strong",
                3:"Very Strong"}.get(strength_points // 4)

    result_string += strength
    # Create a progress bar to visually represent the strength
    result_string += ": [" + "=" * strength_points + "-" * (MAX_POINTS-strength_points) + "] "
    result_string += "{pts}/{total} pts".format(pts=strength_points, total=MAX_POINTS)

    return result_string


print(pass_strength(""))




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