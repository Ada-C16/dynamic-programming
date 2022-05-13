
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
    
    max = None
    current = None

    for i in range(len(nums)):
        
        # get next number
        num = nums[i]

        # update current
        current = num if not current else current + num

        # if there is no max or current sum is > max, replace it
        if not max or current > max:
            max = current

        # if current is negative, start over, it's not adding value to the
        # subarray
        if current < 0:
            current = None

    return max
