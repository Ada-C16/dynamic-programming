
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

    max_sum = cur_sum = nums[0]
    for i in range(1, len(nums)):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        if cur_sum <= 0:
            cur_sum = 0
    return max_sum
