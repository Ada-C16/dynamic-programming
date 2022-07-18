
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
    if len(nums) == 1:
        return nums[0]

    # Initialize the max_sum to the first element in the list.
    max_sum = nums[0]
    # Initialize the current_sum to the first element in the list.
    current_sum = nums[0]
    # Iterate through the list.
    for i in range(1, len(nums)):
        # If the current sum is greater than 0, add the next element to it.
        if current_sum > 0:
            current_sum += nums[i]
        # If the current sum is less than 0, set it to the next element.
        elif current_sum < 0:
            current_sum = nums[i]
        # If the current sum is 0, set it to the next element.
        elif current_sum == 0:
            current_sum = nums[i]
        # If the current sum is greater than the max sum, set the max sum to it.
        if current_sum > max_sum:
            max_sum = current_sum
    # Return the max sum.
    return max_sum


