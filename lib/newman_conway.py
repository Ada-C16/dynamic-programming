
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) because of loop
        Space Complexity: O(n) beause storing previous values
    """
    # no Newman-Conway value for zero
    # base case is for 1 and 2 and returns 1
    
    if num == 0:
        raise ValueError("No Newman-Conway value for zero")

    if num == 1:
        return '1'
    
    memo = [0, 1, 1]
    
    # need to start range at index 3 after base cases
    # loop thru to append value to memo for each index
    for i in range(3, num + 1):
        nc_value = memo[memo[i - 1]] + memo[i - memo[i - 1]]
        memo.append(nc_value)

    return ' '.join([str(item) for item in memo[1:]])
    
    