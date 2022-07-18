
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: On
        Space Complexity: ON
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    max_sub_array = nums[0]
    max_sub = nums[0]

    for i in range(1,len(nums)):

        max_sub = max(max_sub + nums[i], nums[i])
        max_sub_array = max(max_sub_array, max_sub)
  
    return max_sub_array