

# Time complexity: ?
# Space Complexity: ?
from multiprocessing.sharedctypes import Value


def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError
    elif num == 1:
        return "1"
    elif num == 2:
        return "1 1"

    memo_list = [0,1,1]

    for n in range(3, num +1):
        new_num = memo_list[memo_list[n-1]] + memo_list[n - memo_list[n-1]]
        memo_list.append(new_num)
    memo_list.pop(0)
    memo_list = " ".join([str(x) for x in memo_list])
    return memo_list


