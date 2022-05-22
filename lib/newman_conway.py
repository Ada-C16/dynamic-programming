
#### -------------------- NON MEMOIZED -------------------- #### 
# # Time complexity: ?
# # Space Complexity: ?
# def newman_conway(num):
#     """ Returns a list of the Newman Conway numbers for the given value.
#         Time Complexity: O(n)
#         Space Complexity: O(n)
#     """
#     if not num:
#         raise ValueError
#     return " ".join([str(helper(x)) for x in range(1, num+1)])

# def helper(n):
#     if n==1 or n==2:
#         return 1
#     return helper(helper(n - 1)) + helper(n - helper(n - 1))

#### ---------------------- MEMOIZED ---------------------- #### 
# Time complexity: O(n)
# Space Complexity: O(n)
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if not num:
        raise ValueError
    memo={1:1, 2:1}
    for i in range(3, num+1):
        memo[i]=memo[memo[i-1]]+memo[i-memo[i-1]]
    return " ".join((str(memo[x]) for x in range(1, num+1)))
