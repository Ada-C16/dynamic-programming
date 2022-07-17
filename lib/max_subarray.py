
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    max = - 10000000000000000000000000000000000000000000
    curr_max = 0

    for num in nums:
        curr_max += num
        if curr_max > max:
            max = curr_max
        if curr_max < 0:
            curr_max = 0
    return max


