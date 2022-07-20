# Time complexity: ?
# Space Complexity: ?


def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    nc_nums = [1, 1]
    if num < 1:
        raise ValueError("Num must be greater than 0.")
    for i in range(2, num + 1):
        nc_nums.append(nc_nums[nc_nums[i - 1] - 1] + nc_nums[i - nc_nums[i - 1]])
    string_list = []
    for n in nc_nums:
        string_list.append(str(n))
    return " ".join(string_list[0:num])

    # pass