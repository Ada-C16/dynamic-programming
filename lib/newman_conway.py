# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    nc_array = [0, 1, 1]
    nc_string = "1 1"

    if num <= 0:
        raise ValueError()

    if num == 1: 
        return str(num)

    if num == 2: 
        return nc_string

    for i in range(3, num + 1):
        new_num = nc_array[nc_array[i - 1]] + nc_array[i - nc_array[i - 1]]
        nc_array.append(new_num)
        nc_string += " " + str(new_num)

    return nc_string