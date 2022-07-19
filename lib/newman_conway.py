
import array
# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: o(n)
        Space Complexity: o(n)
    """
    # to store values 
    if num < 1: 
        raise ValueError ("Invalid Num")
    if num == 1: 
        return "1"

    f = [0, 1, 1]
    output = "1"

    count = 3 
    # To store values of sequence in array

    while count <= num: 
        f.append(f[f[count - 1]]+ f[count - f [ count -1]])
        count += 1 
    number = [str(item) for item in f]
    
    return " ".join(number[1:])
    # for i in range(3, num + 1):
    #     r = f[f[i-1]]+f[i-f[i-1]]
    #     f.append(r);
 
    # return r