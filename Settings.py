"""
This file allows allow tuning the parameters of entropy and toggling of specific features.

Settings:
    MUTATION:
        Default: True
        Should mutation occur?
        To turn off individual types, set their mutation rates to 0.

    FLOAT_MUTATION_RATE:
        Default: 0.05
        A random number between 0 and 1 is scaled down by the mutation rate and then scaled again by the value itself

    INTEGER_MUTATION_RATE:
        Default: 2
        Integer Mutation rate must be an integer.
        If Mutation rate is 1 then there is stability at 1 and all numbers will hover around 1 on average, but may fluctuate to higher values.
        If Mutation rate is 2, then numbers change by twice their value on average leading to exponential fluctuations. 3 for thrice, etc.

    CHAR_MUTATION_RATE:
        Default: 0.004
        the default value is tuned to make only 1 or 2 chars drift per read in a strings about the size of sentence.
        As a result, individual chars drift rather slowly.

    BOOLEAN_MUTATION_RATE:
        Default: 0.05
        Boolean_Mutation_rate represents the chance to mutate where 0 is never and 1 is can mutate everytime.
        This is different behavior than the other mutation_rates which control how much the value mutates by.
        the default value corresponds to a 5% chance of changing.
        WARNING: Higher values make programs pretty unstable. While loops and if statements may just decide
        to not run if the boolean decays to false when it should have been true. Debugging that can be quite hard.
"""

# Default: True
# Should mutation occur?
# To turn off individual types, set their mutation rates to 0.
MUTATION = True

# Default: 0.05
# A random number between 0 and 1 is scaled down by the mutation rate and then scaled again by the value itself
FLOAT_MUTATION_RATE = 0.05

# Default: 1
# If Mutation rate is 1 then there is stability at 1 and all numbers will hover around 1 on average, but may fluctuate to higher values.
# If Mutation rate is 2, then numbers change by twice their value on average leading to exponential fluctuations. 3 for thrice, etc.
INTEGER_MUTATION_RATE = 1

# Default: 0.004
# the default value is tuned to make only 1 or 2 chars drift per read in a strings about the size of sentence.
# As a result, individual chars drift rather slowly.
CHAR_MUTATION_RATE = 0.004

# Default: 0.05
# Boolean_Mutation_rate represents the chance to mutate where 0 is never and 1 is can mutate everytime.
# This is different behavior than the other mutation_rates which control how much the value mutates by.
# the default value corresponds to a 5% chance of changing.
# WARNING: Higher values make programs pretty unstable. While loops and if statements may just decide
# to not run if the boolean decays to false when it should have been true. Debugging that can be quite hard.
BOOLEAN_MUTATION_RATE = 0.05


def get_mutation_rate(for_type):
    """
    Returns the mutation rate for the passed in type, taking whether mutation is on/off into account. Not Case Sensitive

    Args:
        for_type (str): a string representing the entropy type.
            Valid values are "Float", "Integer", "Char", and "Boolean".

    Returns:
        float/int: the mutation rate. 0 if type was not found or mutation is off.

    Raises:
        KeyError: Raises an exception.
    """

    for_type = for_type.upper()
    if MUTATION:
        try:
            return globals()[for_type + "_MUTATION_RATE"]
        except KeyError:
            print("Was unable to locate mutation rate for type " + for_type)  #Todo: add better error handling. Print statements aren't the best way to handle it.
            return 0
    else:
        return 0

