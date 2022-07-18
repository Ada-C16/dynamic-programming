

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num == 0:
        raise ValueError("Input must be greater than 0.")

    if num == 1:
        return "1"

    if num == 2:
        return "1 1"

    # Initialize the list of numbers.
    numbers = [1, 1]

    for i in range(2, num + 1):
        numbers.append(numbers[numbers[i - 1] - 1] + numbers[i - numbers[i - 1]])

    # Return the list of numbers.
    return " ".join(str(x) for x in numbers [0:num])
    