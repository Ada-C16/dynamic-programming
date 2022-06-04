

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    # P(n) = P(P(n - 1)) + P(n - P(n - 1)) - Newman Conway Sequence
    if num == 0:
        raise ValueError()

    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    starter_arr = [0, 1, 1]

    i = 3
    while i <= num:
        starter_arr.append(
            starter_arr[starter_arr[i-1]] + starter_arr[i - starter_arr[i-1]])
        i += 1

    newman_string = ""
    for i in range(1, len(starter_arr)):
        newman_string += str(starter_arr[i]) + " "

    return newman_string[:-1]
