
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n) - loops through the array once
        Space Complexity: O(1)
    """
    
    max = None
    current = 0

    for i in range(len(nums)):

        # update current
        current += nums[i]

        # if there is no max or current sum is > max, replace it
        if not max or current > max:
            max = current

        # if current is negative, start over, it's not adding value to the
        # subarray
        if current < 0:
            current = 0

    return max if max else 0
