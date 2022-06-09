def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError
    
    if num == 1:
        return '1'

    if num == 2:
        return '1 1'
    
    sequence = [0, 1, 1]

    for i in range (3, num + 1):
        sequence.append( sequence[sequence[i-1]] + sequence[i - sequence[i-1]])
        
    return " ".join([str(item) for item in sequence[1:num+1]])