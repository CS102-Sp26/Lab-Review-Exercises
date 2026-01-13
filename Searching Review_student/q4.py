def findMissingNumber(nums):
    """
    Identifies the missing number in a descending sequence using binary search.

    Args:
        nums (list): A descending list of integers with one missing value.

    Returns:
        int: The missing integer from the sequence.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(findMissingNumber([4, 3, 2, 1]))              # Should print: 5
print(findMissingNumber([4, 3, 2]))                 # Should print: 1 
print(findMissingNumber([6, 5, 3, 2, 1]))           # Should print: 4
print(findMissingNumber([6, 4, 3, 2, 1]))           # Should print: 5
print(findMissingNumber([9, 8, 7, 6, 5, 4, 3, 1]))  # Should print: 2 
print(findMissingNumber([9, 8, 7, 6, 5, 3, 2, 1]))  # Should print: 4
print(findMissingNumber([8, 7, 6, 5, 4, 3, 2, 1]))  # Should print: 9 

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py