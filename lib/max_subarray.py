
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
    
    # [-2,1,-4,5,6]  -> 11
    # [-2,-1] -> -1
    
    max_sum = nums[0]
    temp_sum = 0
    for num in nums: # 6
        temp_sum += num # 11
        if temp_sum > max_sum :
            max_sum = temp_sum  # 11
        if temp_sum < 0:
            temp_sum = 0 
    return max_sum 
