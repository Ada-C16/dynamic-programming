

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) - Where n is the num passed to the function
        Space Complexity: O(n)
    """
    if num <= 0:
        raise ValueError("num must be > 0")

    if num == 1:
        return "1"

    newman_nums = [None] * (num)

    newman_nums[0] = 1
    newman_nums[1] = 1

    n = 2
    while n < num:
        newman_nums[n] = newman_nums[newman_nums[n - 1] - 1] + newman_nums[n  - newman_nums[n-1]]
        n += 1

    str_response = " ".join(map(str, newman_nums))

    return str_response
    
