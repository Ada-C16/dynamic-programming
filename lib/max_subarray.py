
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n)
        Space Complexity: 0(1)
    """
    if nums == None or len(nums) == 0:
        return 0
    
    # building memo
    max_sub_array = [0] * len(nums)

    # establishing base case
    max_sub_array[0] = nums[0]

    for i in range(1, len(nums)):
        # finding the max of the subarray compared to the current value in nums
        max_sub_array[i] = max(max_sub_array[i - 1] + nums[i], nums[i])
    return max(max_sub_array)
