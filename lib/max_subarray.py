
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
    else:
        temp_sum = nums[0]
        max_sum = max(nums)
        for i in range(1,len(nums)):
            if nums[i] > temp_sum + nums[i]:
                temp_sum = nums[i]
            else:
                temp_sum = temp_sum + nums[i]
            max_sum = max(max_sum, temp_sum)
        return max_sum