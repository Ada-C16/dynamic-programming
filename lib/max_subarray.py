
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    max_so_far = 0
    max_ending_here = 0

    for val in nums:
        max_ending_here += val

        if max_ending_here < 0:
            max_ending_here = 0
        max_so_far = max(max_so_far, max_ending_here)
    
    if max_so_far == 0:
        return max(nums)

    return max_so_far