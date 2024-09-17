def LCS(string1, string2):
    # Create the matrix we use to store matching values
    matrix = [[0 for i in range(len(string2)+1)] for i in range(len(string1)+1)]
    # Iterate through the matrix
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            # When we have a match we take the diagonal value and increment by 1 since we have a new match
            if string1[i-1] == string2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            # Otherwise we just keep the same diagonal values
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])


    # Find the matching letters in the string:
    # Create a way to save the values as LCS tracker
    lcsTracker = []
    # Since we are climbing through the table we need to have values to remove
    i = len(string1)
    j = len(string2)
    # While we still have colmuns and rows we iterate through
    while i > 0 and j > 0:
        # If we have a match then we know that that is a matching val so we add it then iterate
        if string1[i-1] == string2[j-1]:
            lcsTracker.append(string1[i-1])
            i -= 1
            j -= 1
        # If i-1 is less then we iterate along i for when it is higher
        elif matrix[i-1][j] > matrix[i][j-1]:
            i -= 1     
        # If not we just move onto the next in j
        else:
            j -= 1
    # Print our results
    print("Length of matching LCS: {}".format(matrix[len(string1)][len(string2)]))
    print("LCS: {}".format(lcsTracker))
    print("Matrix: ")
    pp.pprint(matrix)
LCS("apple", "apples")