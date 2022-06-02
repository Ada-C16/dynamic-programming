

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num < 1:
        raise ValueError("num must be greater than 0")

    if num == 1:
        return "1"

    sequence = [0, 1, 1]
    result = "1 1"

    for n in range(3, num + 1):
        # memo = previous__number + (current_number + previous_number)
        val = sequence[sequence[n - 1]] + sequence[n - sequence[n - 1]]
        sequence.append(val)
        result += " " + str(val)

    return result

    # P(n) = P(P(n - 1)) + P(n - P(n - 1))
