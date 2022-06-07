
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
        
    final_max = nums[0]
    temp_max = nums[0]

    for i in range(1, len(nums)):
        temp_max = max(temp_max + nums[i], nums[i])
        if temp_max > final_max:
            final_max = temp_max
    return final_max
