
from multiprocessing.sharedctypes import Value
    
# Time complexity: O(N)
# Space Complexity: O(N)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?

        Input: int
        Output: space separated list of int number of NC nums

        Input : 13
        Output : 1 1 2 2 3 4 4 4 5 6 7 7 8

        P(1) = 1
        P(2) = 1
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))  
    """
    if num == 0:
        raise ValueError
    if num == 1:
        return '1'

    memo = [None] * (num + 1)

    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    i = 3
    while i <= num:
        memo[i] = memo[memo[i-1]] + memo[i - memo[i - 1]]
        i += 1
    
    # add first item and then add " " + next item
    answer = "" + str(memo[1])
    for i in range(2, len(memo)):
        answer += " " + str(memo[i])

    return answer
