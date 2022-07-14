
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: O(1)
    """
    if nums == None or len(nums) == 0:
        return 0
    
    current_sub = 0
    max_sub = nums[0]

    for num in nums:
        if current_sub < 0:
            current_sub = 0
        current_sub += num
        max_sub = max(max_sub, current_sub)
    return max_sub
