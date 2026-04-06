def distance(G , cursed, start_node , end_node):
    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":
    G = {
            'a': [('b', 10), ('d', 10)], 
            'b': [('a', 10), ('c', 10)], 
            'c': [('b', 10), ('d', 10)], 
            'd': [('c', 10), ('a', 10)]
        }

    print(distance(G, ['b'], 'a', 'c'))
    # Should print: (0, 20)

    G = {
            'a': [('b', 5), ('d', 10)],
            'b': [('a', 5), ('c', 10)],
            'c': [('b', 10), ('d', 10)],
            'd': [('c', 10), ('a', 10)]
        }
    
    print(distance(G, ['b', 'd'], 'a', 'c'))
    # Should print: (1, 15)
    

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py