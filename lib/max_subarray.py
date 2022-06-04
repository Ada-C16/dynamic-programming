
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    max_overall = nums[0]
    max_so_far = nums[0]
    for index, num in enumerate(nums):
        so_far_sum = 0
        for each in nums[:index + 1]:
            so_far_sum += each
        max_so_far = max(so_far_sum, num)
        max_overall = max (max_overall, max_so_far)

    return max_overall
  
