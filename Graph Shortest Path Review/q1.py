def cost_wonderland(G):
    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

if __name__ == "__main__":
    G = {
            1: [(2, 60), (4, 120)], 
            2: [(1, 60), (3, 80)], 
            3: [(5, 70), (2, 80)], 
            4: [(1, 120), (5, 150)], 
            5: [(3, 70), (4, 150)]
        }
    
    print(cost_wonderland(G))   # Should print: 80

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py