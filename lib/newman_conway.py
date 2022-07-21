# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    if num == 0:
        raise ValueError
    if num == 1:
        return "1"

    memo = [None] * (num + 1)

    memo[0] = 0
    memo[1] = 1
    memo[2] = 1

    i = 3
    while i <= num:
        memo[i] = memo[memo[i - 1]] + memo[i - memo[i - 1]]
        i += 1

    result = "" + str(memo[1])
    for i in range(2, len(memo)):
        result += " " + str(memo[i])

    return result
