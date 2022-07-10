def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
 # P(1) = 1
    # P(2) = 1
    # for all n > 2
    # P(n) = P(P(n - 1)) + P(n - P(n - 1))
    # use memoization
    if num == 0:
        raise ValueError()
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    new_seq = [0] * (num + 1)
    new_seq[0] = 0
    new_seq[1] = 1
    result = []
    if num > 2:
        new_seq[2] = 1

    i = 3
    # first 3 items
    while i<=num:
        new_seq[i]
        # P(n) = P(P(n - 1)) + P(n - P(n - 1))
        new_seq[i] = new_seq[new_seq[i-1]] + new_seq[i- new_seq[i-1]]
        i +=1

    i = 1
    result = []
    while (i <= num) :
        #  Display the sequence element   
        result.append(new_seq[i])
        i += 1
    resultOutput = [str(item) for item in result]
    return " ".join(resultOutput)