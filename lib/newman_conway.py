def stringify(nmc):
    nmc.pop(0) # O(n)
    nmc = [str(x) for x in nmc] # O(n)
    return " ".join(nmc)

# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    # P(n) = P(P(n - 1)) + P(n - P(n - 1))
    if num == 0:
        raise ValueError()
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    nmc = [None, 1, 1]
    i = 3
    while i <= num : # O(n)
        nmc.append(nmc[nmc[i-1]] + nmc[i - nmc[i-1]])
        i += 1

    return stringify(nmc)
