
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
    i = 0
    while i < len(nums):
        
        # get next number
        num = nums[i]

        # update current
        if not current:
            current = num
        else:
            current += num

        # if current sum is > max, replace it
        if not max or current > max:
            max = current

        # if current is negative, start over
        if current < 0:
            current = None

        # move forward by one
        i += 1

    return max


        

        # get the next number
        # if it is positive, add it to current and compare to max, update if needed
        # if it is negative, compare it to the current. If it is still positive, continue
        # if it is negative, move both pointers up to the next positive num


    # if a subarray of positive numbers is less than the preceeding subarray of 
    # negative numbers, we should split it at the negative numbers because
    # it won't be included in an array to the left, because the negative nums
    # will more than cancel it out. But what if to the right of it there is a 
    # negative 1 and positive 100? Then what? 
    # new thought, if a current sum is higher than the negative group to its right,
    # it should be included because net positive, otherwise, axe it
    # 1  5 -3 -5 6 -1 99 3 | 107 vs 105
    # 50 5 -3 -5 6 -1 99 3 | 107 vs 154
