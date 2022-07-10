

# Time complexity: ?
# Space Complexity: ?
def newman_conway(nums):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n^2)
    """
    if nums == 0:
        raise ValueError

    if nums == 1:
        return "1"
    
    if nums == 2:
        return "1 1"

    seq = ""
    start_list = [0, 1, 1]
    for i in range(3,nums+1): 
        start_list.append( start_list[start_list[i - 1]] + start_list[i - start_list[i - 1]]) 
    
    for num in start_list[1:]:
        seq += str(num) + " "
    return seq.strip()



