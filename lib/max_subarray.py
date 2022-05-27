def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if nums == None or len(nums) == 0:
        return 0

    max_so_far = nums[0]
    max_here = 0

    for num in nums:
        max_here = max_here + num
        if max_here < 0:
            max_here = num
        if max_so_far < max_here:
            max_so_far = max_here
    
    return max_so_far

