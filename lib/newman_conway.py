

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?

        P(n) = P(P(n - 1)) + P(n - P(n - 1))
    """
    # base = ['1','1']
    if num == 0:
        raise ValueError()
    if num == 1:
        return('1')
    # for i in range(num):
    #     if i > 1:
    #         base.append(str(int(base[int(base[i - 1])]) + int(base[i - int(base[i - 1])])))

    # return ' '.join(base)

    f = [0, 1, 1]
    r = 1
    # To store values of sequence in array
    for i in range(3, num + 1):
        r = f[f[i-1]]+f[i-f[i-1]]
        f.append(r)

    return ' '.join([str(j) for j in f[1:]])