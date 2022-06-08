
    # # P(1) = 1
    # # P(2) = 1
    # # for all n > 2
    # # P(n) = P(P(n - 1)) + P(n - P(n - 1))

    # for i in range(2, num + 1):
    #     new_nc_num = nc_nums[nc_nums[i - 1]] + nc_nums[i - nc_nums[i - 1]]
    #     nc_nums.append(new_nc_num)
  

    # string_list = []
    # for n in nc_nums:
    #     string_list.append(str(n))

def sequence(num):
    if num == 1 or num == 2:
        return 1
    else:
        return sequence(sequence(num-1)) + sequence(num -sequence(num-1))

def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Comnewmanslexity: O(n)
        Space Complexity: O(n)
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