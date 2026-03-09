def quick_sort(lst, low, high):
    """
    Sorts a list in-place using the QuickSort algorithm with the random element as the pivot.

    Parameters:
        lst (list): List to sort.
        low (int): Start index.
        high (int): End index.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################
if __name__ == "__main__":
    lst = [5 , 9 , 2 , 1 , 6 , 3 , 0]
    quick_sort(lst, 0, 6)
    print(lst)      # Should print: [0, 1, 2, 3, 5, 6, 9]

    lst = [21 , 36 , 11 , 9 , 6 , 42 , 39]
    quick_sort(lst, 0, 6)
    print(lst)      # Should print: [6, 9, 11, 21, 36, 39, 42]

    lst = []
    quick_sort(lst, 0, -1)
    print(lst)      # Should print: []

    lst = [101]
    quick_sort(lst, 0, 0)
    print(lst)      # Should print: [101]

    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


    

# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q1.py