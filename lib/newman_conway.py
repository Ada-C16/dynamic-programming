def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    if num <= 0:
        raise ValueError

    if num == 1:
        return "1"

    #make an array that is num spaces long 
    sequence = [None] * (num + 1)

    #Must set these up before coding the rest 
    sequence[0] = 0
    sequence[1] = 1
    sequence[2] = 1

    #now, I am starting at position 2 in the index 
    index = 3
    while index <= num:
        sequence[index] = sequence[sequence[index-1]] + sequence[index-sequence[index-1]]
        
        index += 1
    
    string = ""
    i = 1
    while i < (len(sequence)):
        string += str(sequence[i])
        
        if (len(sequence) - i) >= 2:
            string += " "
        i += 1
    
    return(string)
