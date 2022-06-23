

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    if num < 1:
        raise ValueError("Must be a positive number")
    if num == 1:
        return "1"

    current_list = [0, 1, 1]

    count = 3
    while count <= num:
        current_list.append(current_list[current_list[count - 1]] + current_list[count - current_list[count - 1]])
        count += 1

    return [str(item) for item in current_list]
