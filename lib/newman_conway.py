

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) ? 
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError("ValueError exception")

    elif num  == 1:
        return "1"
    elif num == 2:
        return "1 1"

    output = "1 1"
    memo = [0,1,1]

    for i in range(3,num+1):
        memo.append(memo[memo[i-1]] + memo[i-memo[i-1]])
    
    output = ""
    for i in range(1,len(memo)):
        output += str(memo[i]) + " "
    return output.strip()