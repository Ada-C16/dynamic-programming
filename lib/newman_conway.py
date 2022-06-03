

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    memo = [None] * (num + 1)
    def helper(cur_num, prev_seq = 1):
        if cur_num > num:
            return
        if cur_num == 1 or cur_num == 2:
            memo[cur_num] = 1
            helper(cur_num + 1)
        else:
            cur_seq = memo[prev_seq] + memo[cur_num - prev_seq]
            memo[cur_num] = cur_seq
            helper(cur_num + 1, cur_seq)

    if num <= 0:
        raise ValueError
    helper(1)
    memo = memo[1:]
    memo = [str(num) for num in memo]
    return " ".join(memo)
