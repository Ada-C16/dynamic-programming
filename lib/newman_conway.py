from ast import Attribute
from multiprocessing.sharedctypes import Value
from types import new_class


def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError
    if num == 1:
        return '1'


    array = [0, 1, 1]
    result = '1 1'

    for i in range(3, num+1):
        newman_conway_value = array[array[i - 1]] + array[i - array[i - 1]]
        array.append(newman_conway_value)
        result += ' ' + str(newman_conway_value)

    return result

"""
P(1) = 1
P(2) = 1
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1))
"""