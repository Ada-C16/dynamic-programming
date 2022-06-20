
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
    #  initialize maxSub -> first nsumber in the array
    maxSub = nums[0]
    currentSum = nums[0]
    for index in range(1, len(nums)):
        # start at index 1
        # compare current value with current sum
        currentSum = max(nums[index], currentSum + nums[index])
        # assign to the max of itself compared to the currentSum
        maxSub = max(maxSub, currentSum)
    return maxSub
