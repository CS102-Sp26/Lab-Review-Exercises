def BinNumsUsingQueue(n):
    """
    Generates and prints binary numbers from 1 to n using a queue.

    Args:
        n (int): A positive integer specifying the range of numbers.

    Returns:
        None
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

BinNumsUsingQueue(16)
''' Should print:
1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000
'''

BinNumsUsingQueue(50)
''' Should print:
1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000 
10001 10010 10011 10100 10101 10110 10111 11000 11001 11010 11011 11100 
11101 11110 11111 100000 100001 100010 100011 100100 100101 100110 100111 
101000 101001 101010 101011 101100 101101 101110 101111 110000 110001 110010
'''

##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q3.py