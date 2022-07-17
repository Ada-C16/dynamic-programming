

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    def newman_helper(cur_num, prev_seq = 1):
        if cur_num > num:
            return
        if cur_num == 1 or cur_num == 2:
            newman_nums[cur_num] = 1
            newman_helper(cur_num + 1)
        else:
            cur_seq = newman_nums[prev_seq] + newman_nums[cur_num - prev_seq]
            newman_nums[cur_num] = cur_seq
            newman_helper(cur_num + 1, cur_seq)

    if num <= 0:
        raise ValueError
        
    newman_nums = [None] * (num + 1)
    
    newman_helper(1)

    newman_nums = newman_nums[1:]
    final_string = f'{newman_nums.pop(0)}'
    for num in newman_nums:
        final_string += ' ' + str(num)

    return final_string
