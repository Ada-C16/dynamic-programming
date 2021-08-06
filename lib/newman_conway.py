
 

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError("Invalid newman conway number")
    if num == 1:
        return "1"
    
    memo = [0, 1, 1]
    output = "1"

    count = 3
    while count <= num:
        memo.append(memo[memo[count - 1]] + memo[count - memo[count - 1]])
        count += 1

    answer = [str(item) for item in memo]
    return " ".join(answer[1:])
