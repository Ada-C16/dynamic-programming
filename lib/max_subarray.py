
def max_sub_array(nums):
    """ Returns the max subarray of the given list of numbers.
        Returns 0 if  nums is None or an empty list.
        Time Complexity: O(n), iterates through relative to the size of the list given.
        Space Complexity: ? O(1), we will only ever make 2 
    """
    #guard clauses
    if nums == None:
        return 0
    if len(nums) == 0:
        return 0
    
    # initialize /memoize:
    max_subarray_so_far = nums[0]
    max_this_subarray = nums[0]

    for i in range(1, len(nums)): # O(n)
        max_this_subarray = max(max_this_subarray + nums[i], nums[i])
        max_subarray_so_far = max(max_this_subarray, max_subarray_so_far) 

    return max_subarray_so_far 