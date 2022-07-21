

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    outputs = {}

    res = []
    if num <= 0:
        raise ValueError

    for n in range(1, num + 1):
        if n == 1 or n ==2:
            outputs[n] = 1
            res.append("1")
            continue

        val = outputs[outputs[n-1]] + outputs[n - outputs[n - 1]]
        outputs[n] = val
        res.append(str(val))

    return " ".join(res)
