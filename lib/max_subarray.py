
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    if nums == None:
        return 0
    elif len(nums) == 0:
        return 0
    
    all_maxes = nums[0]
    max_current_sub = nums[0]

    for i in range(1, len(nums)):
        max_current_sub = max(max_current_sub + nums[i], nums[i])
        all_maxes = max(all_maxes, max_current_sub)

    return max_current_sub


