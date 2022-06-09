def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num <= 0:
        raise ValueError 
    elif num == 1:
        return '1' 
    else: 
        memo = [0, 1, 1]
        for i in range(3, num+1):
            next_num = memo[memo[-1]] + memo[i-memo[i-1]]
            memo.append(next_num)
        return ' '.join([str(i) for i in memo if i])
