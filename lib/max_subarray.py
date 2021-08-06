
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    max_subarray_so_far = nums[0]
    max_this_sub_array = nums[0]

    for i in range(1, len(nums)):
        max_this_sub_array = max(max_this_sub_array + nums[i], nums[i])
        max_subarray_so_far = max(max_subarray_so_far, max_this_sub_array)

    return max_subarray_so_far
    