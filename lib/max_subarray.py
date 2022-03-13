import math
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
    largest_sum = [0] * len(nums)
    largest_sum[0] = nums[0]

    for i in range(1, len(nums)):
        if largest_sum[i - 1] <= 0:
            largest_sum[i] = nums[i]
            
        else:
            largest_sum[i] = nums[i] + largest_sum[i-1]
           
    return max(largest_sum)
        

