def string_reversal(s):
    """
    Reverses a string using a stack.

    Args:
        s (str): The input string to reverse.

    Returns:
        str: The reversed string.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(string_reversal('Alive is awesome'))  # Should print: emosewa si evilA 
print(string_reversal('Hello World!!'))     # Should print: !!dlroW olleH
print(string_reversal('Data structures'))   # Should print: serutcurts ataD 
print(string_reversal('Be in present'))     # Should print: tneserp ni eB
print(string_reversal('hello'))             # Should print: olleh 
print(string_reversal('Howdy'))             # Should print: ydwoH
print(string_reversal(''))                  # Should print:  
print(string_reversal('a'))                 # Should print: a 

# ##################################################################
# # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
# ##################################################################


# # Testing For all testcases 
# # In order to test your function, type the following command on the terminal:
# # pytest tests/test_q1.py