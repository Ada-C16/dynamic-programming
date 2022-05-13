# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """Returns a list of the Newman Conway numbers for the given value.
    Time Complexity: ?
    Space Complexity: ?
    """
    if num <= 0:
        raise ValueError

    if num == 1:
        return "1"

    nums = [0, 1, 1]

    i = 3
    while i <= num:
        nums.append(nums[nums[i - 1]] + nums[i - nums[i - 1]])
        i += 1

    return " ".join([str(n) for n in nums[1:]])
