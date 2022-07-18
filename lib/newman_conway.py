

# Time complexity: o(n)
# Space Complexity: o(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: o(n)
        Space Complexity: o(n)
    """
    nc_list = [0] * (num + 1)
    if num == 0:
        raise ValueError("n must be > 0")
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    if num > 2:
        nc_list[1] = 1
        nc_list[2] = 1
        for i in range(3, num + 1):
            
            nc_list[i] = nc_list[nc_list[i-1]] + nc_list[i - nc_list[i-1]]

        return " ".join(str(v) for v in nc_list[1:])
print(newman_conway(1))

