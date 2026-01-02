def mirror(queue):
    """
    Appends the reverse of a queue's contents to itself using a stack if needed.
    
    Args:
    queue (list[str]): A queue of strings to mirror.
    
    Returns:
    list[str]: The queue after appending its reversed contents.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(mirror(['a', 'b', 'c']))          # Should print: ['a', 'b', 'c', 'c', 'b', 'a'] 
print(mirror(['PFun', 'DSA', 'OOP']))   # Should print: ['PFun', 'DSA', 'OOP', 'OOP', 'DSA', 'PFun']

# ##################################################################
# # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
# ##################################################################


# # Testing For all testcases 
# # In order to test your function, type the following command on the terminal:
# # pytest tests/test_q2.py