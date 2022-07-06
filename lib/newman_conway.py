

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?

        P(1) = 1
        P(2) = 1
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))
    """

    # make a dict with key as n, and the value as P(n) (aka the output)

    outputs = {}

    res = []
    if num <= 0:
        raise ValueError
    
    for n in range(1, num + 1):
        if n == 1 or n == 2:
            outputs[n] = 1
            res.append("1")
            continue
        # P(n -1) -> outputs[ n - 1]
        value = outputs[outputs[n - 1]] + outputs[n - outputs[n - 1]]
        outputs[n] = value
        res.append(str(value))
    
    return " ".join(res)
