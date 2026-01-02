def postfixEval(exp):
    """
    Evaluates a postfix arithmetic expression using a stack.

    Args:
        expr (str): A string representing a valid postfix expression.

    Returns:
        float: The result of evaluating the expression.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(postfixEval('2 1 - 3 4 2 / + *')) # Should print: 5.0
print(postfixEval('2 3 4 + * 6 -'))     # Should print: 8 
print(postfixEval('3 5 -'))             # Should print: -2 
print(postfixEval('6 2 *'))             # Should print: 12
print(postfixEval('2 3 + 4 2 - *'))     # Should print: 10 
print(postfixEval('2 3 1 * + 9 -'))     # Should print: -4 
print(postfixEval('2 3 * 1 +'))         # Should print: 7 

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q5.py