

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num == 1 or num == 2: 
        return 1 
    else: 
        return newman_conway(newman_conway(num - 1)) + newman_conway(num - newman_conway(num-1))