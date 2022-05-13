
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

    max_so_far = -9999999
    max_ending_here = 0

    i = 0
    while i < len(nums):
        max_ending_here += nums[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
        
        print(max_ending_here)
        print(max_so_far)
        i += 1
    
    return max_so_far

max_sub_array([-3, -4, -5, -6, -7])
    
