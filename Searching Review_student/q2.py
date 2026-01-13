def getTopIndex_UnimodelSequence(unimodel_sequence):
    """
    Finds the index of the top element in a unimodal sequence.

    Args:
        arr (list): A unimodal list of integers.

    Returns:
        int: Index of the maximum element in the sequence.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(getTopIndex_UnimodelSequence([1, 3, 5, 9, 4, 1]))                 # Should print: 3
print(getTopIndex_UnimodelSequence([1, 3, 5, 9, 4]))                    # Should print: 3 
print(getTopIndex_UnimodelSequence([10, 12, 20, 32, 37, 35, 30, 25]))   # Should print: 4 
print(getTopIndex_UnimodelSequence([10, 12, 20, 32, 35, 30, 25]))       # Should print: 4
print(getTopIndex_UnimodelSequence([1, 10, 12, 15, 5, 3, 2]))           # Should print: 3 

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q2.py