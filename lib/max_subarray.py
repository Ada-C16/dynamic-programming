def max_sub_array(nums):

    if nums == None:
        return 0
    if len(nums) == 0:
        return 0

    max_array = nums[0]
    current_max = nums[0]

    for i in range(1, len(nums)):
        current_max = max(nums[i], current_max + nums[i])
        max_array = max(current_max, max_array)
    return max_array
