

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    # P(1) = 1
    # P(2) = 1
    # for all n > 2
    # P(n) = P(P(n - 1)) + P(n - P(n - 1))
    # use memoization table to store values fot each calcula item
    if num == 0:
        raise ValueError()
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    record = [0] * (num + 1)
    record[0] = 0
    record[1] = 1
    result = []
    if num > 2:
        record[2] = 1
    
    i = 3
    # first 3 items
    while i<=num:
        record[i]
        # P(n) = P(P(n - 1)) + P(n - P(n - 1))
        record[i] = record[record[i-1]] + record[i- record[i-1]]
        i +=1

    i = 1
    result = []
    while (i <= num) :
        #  Display the sequence element   
        result.append(record[i])
        i += 1
    resultOutput = [str(item) for item in result]
    return " ".join(resultOutput)
