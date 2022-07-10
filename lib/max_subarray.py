
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
    maxSub = nums[0]
    currentSum = nums[0]
    for index in range(1, len(nums)):
        currentSum = max(nums[index], currentSum + nums[index])
        maxSub = max(maxSub, currentSum)
    return maxSub
