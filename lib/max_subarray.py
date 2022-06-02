
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
    cur_sub=max_sub=nums[0]
        
    for num in nums[1:]:
        cur_sub = max(num,cur_sub+num)
        max_sub = max(max_sub,cur_sub)
            
    return max_sub
