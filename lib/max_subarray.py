def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)?
        Space Complexity: constant?
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    current_max_array = nums[0]
    max_sub_array = nums[0]

    for i in range(1, len(nums)):
        max_sub_array = max(max_sub_array + nums[i], nums[i])
        current_max_array = max(current_max_array, max_sub_array)

    return current_max_array
