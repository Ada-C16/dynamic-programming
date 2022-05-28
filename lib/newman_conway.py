def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError("invalid number")
    if num == 1:
        return "1"
    
    sequence = [0, 1, 1]

    for i in range(3, num + 1):
        sequence.append(sequence[sequence [i - 1]] + sequence[i - sequence[i - 1]])
    
    newman_conway_nums = [str(num) for num in sequence]
    return " ".join(newman_conway_nums[1:])