
from json.encoder import INFINITY


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

    maximum = - INFINITY
    current_max = 0

    for num in nums:
        current_max += num
        if current_max > maximum:
            maximum = current_max
        if current_max < 0:
            current_max = 0
    return maximum
