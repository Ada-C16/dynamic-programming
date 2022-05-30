

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    # Newman Conway numbers:
    # P(1) = 1
    # P(2) = 1
    # For all n >2, P(P(n - 1)) + P(n - P(n - 1))

    # Fib example:
    # Fib(0) = 0
    # Fib(1) = 1
    # Fib(n) = Fib( n - 1) + Fib(n-2) for all n > 1
    # def fib(n):
    #     fibs = [0, 1]
    #     for i in range(2, n + 1):
    #         fibs.append(fibs[i - 1] + fibs[i - 2])
    #     return fibs[n]

    nc_nums = [1, 1]

    if num < 1:
        raise ValueError("Num must be greater than 0.")

    for i in range(2, num + 1):
        nc_nums.append(nc_nums[nc_nums[i - 1] - 1] + nc_nums[i - nc_nums[i - 1]])

    string_list = []
    for n in nc_nums:
        string_list.append(str(n))

    return " ".join(string_list[0:num])
