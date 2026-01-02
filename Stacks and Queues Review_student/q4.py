def Infix_to_Prefix(expression):
    """
    Converts an arithmetic expression from infix to prefix notation.

    Args:
        expr (str): A string representing a valid arithmetic expression in infix notation.

    Returns:
        str: The corresponding expression in prefix notation.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(Infix_to_Prefix('( A + B ) * ( C + D )')) # Should print: * + A B + C D 
print(Infix_to_Prefix('A * B + C * D'))         # Should print: + * A B * C D
print(Infix_to_Prefix('A * B + C'))             # Should print: + * A B C
print(Infix_to_Prefix('A * ( B + C )'))         # Should print: * A + B C
print(Infix_to_Prefix('A - B'))                 # Should print: - A B
print(Infix_to_Prefix('A + B * C'))             # Should print: + A * B C
print(Infix_to_Prefix('( A + B ) * C'))         # Should print: * + A B C

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q4.py