

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError("invalid num")
    
    if num == 1:
        return "1"
    
    list = [0,1,1]
    count = 3
    while num >= count:
        list.append(list[list[count-1]]+list[count - list[count-1]])
        count += 1

    answer = [str(item) for item in list]
    return " ".join(answer[1:])
