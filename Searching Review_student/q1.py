def length_of_line(points_lists, length):
    """
    Processes a list of lines to find a required length
    using Binary Search.

    Args:
        points_lists (list): Input list containing line coordinate pairs.
        length (float): Length value to be checked.

    Returns:
        int: Index of the matching line, or -1 if not found.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(length_of_line([
                        [(2,4),(4,6)], 
                        [(1,2),(4,6)], 
                        [(4,0),(6, 6)]
                    ], 5.0))
# Should print: 1

print(length_of_line([ 
                        [(2,4),(4,6)], 
                        [(1,2),(4,6)],
                        [(4,0),(6, 6)]
                    ], 6.32))
# Should print: 2

print(length_of_line([ 
                        [(2,4),(4,6)], 
                        [(1,2),(4,6)],
                        [(4,0),(6, 6)]
                    ], 1.0))
# Should print: -1

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:

# pytest tests/test_q1.py
