

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    if num < 1:
        raise(ValueError)
    elif num == 1:
        return '1'
    elif num == 2:
        return '1 1'

    memo = [None] * (num + 1)
    memo[1] = 1
    memo[2] = 1

    for i in range(3, num + 1):
        memo[i] = memo[memo[i - 1]] + memo[i - memo[i - 1]]

    result = str(memo[1])
    for i in range(2, len(memo)):
        result += " " + str(memo[i])
    return result

