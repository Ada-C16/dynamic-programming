
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: 0(n)
        Space Complexity: 0(1)
    """
    
     # compare sum of current subarray as iterating thru array, remove subarrays with negative sum, keep track of max sum at each index
     
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    currentMaxSum = 0
    maxSubArray = nums[0]

    for i in range(len(nums)):
        currentMaxSum = max(nums[i], currentMaxSum + nums[i])
        maxSubArray = max(maxSubArray, currentMaxSum)

    return maxSubArray
