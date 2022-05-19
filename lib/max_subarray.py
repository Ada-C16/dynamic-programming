
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: ?
        Space Complexity: ?
        (a) max_ending_here = max_ending_here + a[i]
        (b) if(max_ending_here < 0)
            max_ending_here = 0
        (c) if(max_so_far < max_ending_here)
            max_so_far = max_ending_here
        return max_so_far
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    max_so_far = 0
    max_ending_here = 0
    i = 0

    while i < len(nums):
        max_ending_here = max_ending_here + nums[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if (max_ending_here < 0):
            max_ending_here = 0
        i += 1
    if max_so_far == 0:
        max_so_far = max(nums)
    
    return max_so_far
