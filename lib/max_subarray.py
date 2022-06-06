
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
    
    ans = nums[0]
    subarr_sum = nums[0]

    for i in range(1, len(nums)):
        subarr_sum = max(nums[i], nums[i] + subarr_sum)
        ans = max(ans, subarr_sum)

    return ans
