
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
    pass

    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = 0
        current_sum += nums[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum