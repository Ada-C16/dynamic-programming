
# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError
    if num == 1:
        return "1"
    if num == 2:
        return "1 1"
    initial_array =  [0, 1, 1]
    for i in range(3, num + 1):
        r = initial_array[initial_array[i-1]]+initial_array[i-initial_array[i-1]]
        initial_array.append(r)
    # remove the first 0 using list slices and change elements to str
    stringified_array = []
    for elem in initial_array[1:]:
        stringified_array.append(str(elem))
    return " ".join(stringified_array)

