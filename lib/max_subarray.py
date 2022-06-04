
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

    max_sum = nums[0]
    temp_sum = nums[0]

    for i in range(1, len(nums)):
        current = nums[i]
        temp_sum = max(current, current + temp_sum)
        max_sum = max(temp_sum, max_sum)

    return max_sum
