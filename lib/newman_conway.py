def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)?
        Space Complexity: O(n)?
    """
    if num < 1:
        raise ValueError("Invalid newman conway number")
    if num == 1:
        return "1"

    n = [0, 1, 1]

    count = 3
    while count <= num:
        n.append(n[n[count - 1]] + n[count - n[count - 1]])
        count += 1

    return ' '.join([str(item) for item in n[1:]])
