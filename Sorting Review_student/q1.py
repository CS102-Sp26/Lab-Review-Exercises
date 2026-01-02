def sort_matrix_by_row(lst):
    """
    Processes a matrix and returns a sorted result.

    Args:
        matrix (list): Input matrix.

    Returns:
        list: Processed matrix.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(sort_matrix_by_row([
                            [5, 8, 1], 
                            [6, 7, 3], 
                            [5, 4, 9]
                        ]))
''' Should print:
                        [
                            [1, 5, 8], 
                            [3, 6, 7], 
                            [4, 5, 9]
                        ]
'''

print(sort_matrix_by_row([
                            ['chair', 'table', 'house'], 
                            ['square', 'rectangle', 'triangle'], 
                            ['motor cycle', 'car', 'truck']
                        ]))
''' Should print:
                        [
                            ['chair', 'house', 'table'], 
                            ['rectangle', 'square', 'triangle'], 
                            ['car', 'motor cycle', 'truck']
                        ]
'''

print(sort_matrix_by_row([
                            [75, 28, 12], 
                            [63, 37, 23], 
                            [84, 15, 49]
                        ]))
''' Should print:
                        [
                            [12, 28, 75], 
                            [23, 37, 63], 
                            [15, 49, 84]
                        ]
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py