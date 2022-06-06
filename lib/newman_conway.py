# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
Newman-Conway Sequence is the one which generates the following integer sequence. 
1 1 2 2 3 4 4 4 5 6 7 7…
In mathematical terms, the sequence P(n) of Newman-Conway numbers is defined by recurrence relation 

P(n) = P(P(n - 1)) + P(n - P(n - 1)) 
with seed values P(1) = 1 and P(2) = 1
Given a number n, print n-th number in Newman-Conway Sequence.
    """
    if num == 0:
        raise ValueError
    elif num == 1:
        return "1"
    elif num == 2:
        return "1 1"

    memo_list = [0,1,1]

    for n in range(3, num +1):
        new_num = memo_list[memo_list[n-1]] + memo_list[n - memo_list[n-1]]
        memo_list.append(new_num)
    memo_list.pop(0)
    memo_list = " ".join([str(x) for x in memo_list])
    return memo_list

        

    


