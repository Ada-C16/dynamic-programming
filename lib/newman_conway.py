def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
        P(1) = 1 at 1st index?
        P(2) = 1 at 2nd index?
        for all n > 2
        P(n) = P(P(n - 1)) + P(n - P(n - 1))
    """
    result = []
    result_string = ""
    if num <= 0:
        raise ValueError
    if num == 1:
        return "1"
    elif num == 2:
        return "1 1"

    # memo of subproblems
    newman_memo = [0, 1, 1]
    
    number = 3 # number has to be greater than 2 to do the recursive formula
    while number <= num:
        newman_memo.append(newman_memo[newman_memo[number-1]]+ newman_memo[number-newman_memo[number-1]])
        number += 1

    for item in newman_memo:
        result.append(str(item))
    
    result_string = " ".join(result[1:])
    print(result_string)
    return result_string 
