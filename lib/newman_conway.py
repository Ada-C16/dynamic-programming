

# Time complexity: ?
# Space Complexity: ?
from multiprocessing.sharedctypes import Value


def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError

    if num == 1:
        return str(num)

    p = [0, 1, 1]
    s = "1 1"

    for n in range(3, num + 1):
        val = p[p[n - 1]] + p[n - p[n - 1]]
        p.append(val)
        s += " " + str(val)

    return s