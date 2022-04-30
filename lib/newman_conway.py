

# Time complexity: O(n)
# Space Complexity: O(n)

    
def newman_conway(num):
    if num == 0:
        raise ValueError

    memo_arr = [0, 1, 1]
    
    for i in range(3, num + 1):
        memo_arr.append(memo_arr[memo_arr[i-1]] + memo_arr[i - memo_arr[i - 1]])

    res_str = ""
    for j in range(1, num+1):    
        res_str += str(memo_arr[j]) + " "
        
    res_str = res_str[:-1]
    return res_str