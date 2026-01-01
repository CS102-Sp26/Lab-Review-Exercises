def blur_image(A):
    """
    Blurs a 2D image using local neighbor averaging.

    Args:
        A (list[list[float]]): Input image.

    Returns:
        list[list[float]]: Blurred image.
    """

    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

print(blur_image(
                    [
                        [10, 10, 10, 10, 10], 
                        [20, 20, 20, 20, 20], 
                        [80, 80, 80, 80, 80], 
                        [60, 60, 60, 60, 60], 
                        [70, 70, 70, 70, 70]
                    ]))
''' Should print:
                    [
                        [13.33, 12.5, 12.5, 12.5, 13.33], 
                        [32.5, 30.0, 30.0, 30.0, 32.5], 
                        [60.0, 64.0, 64.0, 64.0, 60.0], 
                        [67.5, 66.0, 66.0, 66.0, 67.5], 
                        [66.67, 67.5, 67.5, 67.5, 66.67]
                    ] 
'''

print(blur_image(
                    [
                        [1, 2, 3], 
                        [4, 5, 6], 
                        [7, 8, 9]
                    ]))
''' Should print:
                    [
                        [2.33, 2.75, 3.67], 
                        [4.25, 5.0, 5.75], 
                        [6.33, 7.25, 7.67]
                    ]
'''

print(blur_image(
                    [
                        [1, 1, 1, 1, 1], 
                        [1, 1, 1, 1, 1], 
                        [1, 1, 1, 1, 1], 
                        [1, 1, 1, 1, 1], 
                        [1, 1, 1, 1, 1]
                    ]))
''' Should print:
                    [
                        [1.0, 1.0, 1.0, 1.0, 1.0], 
                        [1.0, 1.0, 1.0, 1.0, 1.0], 
                        [1.0, 1.0, 1.0, 1.0, 1.0], 
                        [1.0, 1.0, 1.0, 1.0, 1.0], 
                        [1.0, 1.0, 1.0, 1.0, 1.0]
                    ]
'''

# ##################################################################
# # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
# ##################################################################


# # Testing For all testcases 
# # In order to test your function, type the following command on the terminal:
# # pytest tests/test_q2.py