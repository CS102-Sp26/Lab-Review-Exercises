def find_first_and_last(lst, item):
    """
    Searches for the first and last occurrence of an item in a sorted list.

    Args:
        lst (list): A sorted list of items.
        item: The item to be searched.

    Returns:
        tuple or int: A tuple containing the first and last index of the item,
                      or -1 if the item is not found.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(find_first_and_last([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 17))
# Should print: (5, 8)

print(find_first_and_last([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 34))
# Should print: -1

print(find_first_and_last([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19))
# Should print: (9, 9)



##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py