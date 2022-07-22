''' 
P(1) = 1
P(2) = 1
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1)) 
'''

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    # base case guard clauses
    if num < 1:
        raise ValueError('newman conway number cant be zero nums long')
    elif num == 1:
        return '1'
    elif num == 2:
        return '1 1'


    NCnums = [['i']]