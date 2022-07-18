
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

    max_til_now = nums[0]
    max_ending = 0

    for i in range(len(nums)):
        max_ending += nums[i]
        max_til_now = max(max_til_now, max_ending)
        if(max_ending < 0):
            max_ending = 0
    return max_til_now
