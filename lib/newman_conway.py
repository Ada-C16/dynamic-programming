def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError("Input must be greater than 0.")

    if num == 1:
        return "1"
    
    list = [0, 1, 1]
    
    for i in range(3, num + 1):
        list.append(list[list[i-1]] + list[i-list[i-1]])

    return " ".join(str(x) for x in list[1:])