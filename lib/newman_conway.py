''' 
P(1) = 1
P(2) = 1
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1)) 
'''
import array

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: ?
        Space Complexity: ?
    """
    NCnums = [['i']]

newman_conway(5)

# ''' Python program to find the n-th element of
#     Newman-Conway Sequence'''

def sequence(n):
    f = array.array('i', [0, 1, 1])
 
#     # To store values of sequence in array
    for i in range(3, n + 1):
        r = f[f[i-1]]+f[i-f[i-1]]
        f.append(r);
 
#     return r
 
# # Driver code
# def main():
#     n = 10
#     print sequence(n)
     
# if __name__ == '__main__':
#     main()