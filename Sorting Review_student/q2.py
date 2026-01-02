def smallest_absdiff_pairs(lst):
    """
    Processes a list of integers and returns pairs with minimal difference.

    Args:
        nums (list): Input list of integers.

    Returns:
        list: List of element pairs.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(smallest_absdiff_pairs([5, 4, 3, 2]))
# Should print: [(2, 3), (3, 4), (4, 5)]

print(smallest_absdiff_pairs([-20, -3916237, -357920, -3620601, 7374819, -7330761, 
                              30, 6246457, -6461594, 266854, -520, -470]))
# Should print: [(-520, -470), (-20, 30)]

print(smallest_absdiff_pairs([-20, -3916237, -357920, -3620601, 7374819, 
                              -7330761, 30, 6246457, -6461594, 266854]))
# Should print: [(-20, 30)]

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py