

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """

    # p1 = 1
    # p2 = 1
    # for all num > 2
    #     P(n) = P(P(n - 1)) + P(n - P(n - 1))

    if num <= 0:
        raise ValueError("Number must be greater than 0!")

    if num == 1:
        return "1"

    newman_seq = [None] * (num)
    newman_seq[0] = 1
    newman_seq[1] = 1

    n = 2
    while n < num:
        newman_seq[n] = newman_seq[newman_seq[n -1 ] - 1] + newman_seq[n-newman_seq[n - 1]]
        n += 1

    output_seq = " ".join(map(str, newman_seq))
    return output_seq

    

