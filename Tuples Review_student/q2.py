def multipillionaire(sides, goal):
    """
    Return the first player whose accumulated marbles reach a multiple of the goal.

    Args:
        sides (list[int]): Starting marbles for each player.
        goal (int): Target multiple.

    Returns:
        tuple[int, int]: Winning player (1-based) and total rounds.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(multipillionaire([3, 4], 20))
# Should print: (2, 9)

print(multipillionaire([3, 4], 120))
# Should print: (1, 14)

print(multipillionaire([5, 3], 100))
# Should print: (2, 23)

print(multipillionaire([5, 7], 100))
# Should print: (1, 66)

print(multipillionaire([5, 4, 3], 17))
# Should print: (1, 5)

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q2.py