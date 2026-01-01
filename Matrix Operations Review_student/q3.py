def matrixReshape(nums, r, c):
    """
    Reshape a matrix to the given dimensions if possible.

    Args:
        mat: Input matrix.
        r: Target number of rows.
        c: Target number of columns.

    Returns:
        Reshaped matrix, or the original matrix if reshaping is not valid.
    """
    
    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(matrixReshape(
                    [
                        [1, 2], 
                        [3, 4]
                    ], 1, 4))
''' Should print:
                    [
                        [1, 2, 3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2], 
                        [3, 4]
                    ], 2, 3))
''' Should print:
                    [
                        [1, 2], 
                        [3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2, 3, 4, 5]
                    ], 5, 1))
''' Should print:
                    [
                        [1], 
                        [2], 
                        [3], 
                        [4], 
                        [5]
                    ] 
'''

print(matrixReshape(
                    [
                        [1], 
                        [2], 
                        [3], 
                        [4]
                    ], 1, 4))
''' Should print:
                    [
                        [1, 2, 3, 4]
                    ]
'''

print(matrixReshape(
                    [
                        [1, 2, 3, 4], 
                        [5, 6, 7, 8], 
                        [9, 10, 11, 12]
                    ], 2, 6))
''' Should print:
                    [
                        [1, 2, 3, 4, 5, 6], 
                        [7, 8, 9, 10, 11, 12]
                    ] 
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py