
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(1)
        Space Complexity: O(1)
    """
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    max_seen = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        prev = nums[i - 1]
        summed = curr + prev
        curr_max = max(curr, summed)
        nums[i] = curr_max
        if curr_max > max_seen:
            max_seen = curr_max

    return max_seen
    """
    okay, lets see if I remember the algorithm...
    set the maximum to nums[0]
    starting with nums 1
    - sum it with the previous number in the array
    - if the sum of the current number plus the previous number is greater than the number currently in place, update the number at i
    - keep track of the max seen as well
    - return the max seen
    """
