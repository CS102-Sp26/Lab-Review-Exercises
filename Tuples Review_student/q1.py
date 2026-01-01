def spin_the_wheel(standings, jumps):
    """
    Simulate wheel updates until a standing reaches 99.

    Standings are updated simultaneously using fixed jumps modulo 100,
    recorded each round, and the winning player is printed.

    Args:
        standings (tuple[int]): Initial positions.
        jumps (tuple[int]): Increment values.

    Returns:
        list[tuple[int]]: Standings after each update.
    """
    
    # WRITE YOUR CODE HERE
    pass


#############################################################################
# Let's test your code on visible test cases... Run your code file and      #
# check manually whether the code is running as expected...                 #
#############################################################################

import pprint

pprint.pprint(spin_the_wheel((99, 0), (7, 7)))
''' Should print:
Player 0 wins.
[(99, 0)]
'''

print()

pprint.pprint(spin_the_wheel((0, 1), (7, 7)))
''' Should print:
Player 1 wins.
[(0, 1),
 (7, 8),
 (14, 15),
 (21, 22),
 (28, 29),
 (35, 36),
 (42, 43),
 (49, 50),
 (56, 57),
 (63, 64),
 (70, 71),
 (77, 78),
 (84, 85),
 (91, 92),
 (98, 99)]
'''

print()

pprint.pprint(spin_the_wheel((3, 15), (12, 18)))
''' Should print:
Player 0 wins.
[(3, 15),
 (15, 33),
 (27, 51),
 (39, 69),
 (51, 87),
 (63, 5),
 (75, 23),
 (87, 41),
 (99, 59)]
'''

print()

pprint.pprint(spin_the_wheel((32, 23, 79), (7, 11, 97)))
''' Should print:
Player 1 wins.
[(32, 23, 79),
 (39, 34, 76),
 (46, 45, 73),
 (53, 56, 70),
 (60, 67, 67),
 (67, 78, 64),
 (74, 89, 61),
 (81, 0, 58),
 (88, 11, 55),
 (95, 22, 52),
 (2, 33, 49),
 (9, 44, 46),
 (16, 55, 43),
 (23, 66, 40),
 (30, 77, 37),
 (37, 88, 34),
 (44, 99, 31)]
 '''

print()

pprint.pprint(spin_the_wheel((30, 47, 39), (54, 66, 6)))
''' Should print:
Player 2 wins.
[(30, 47, 39),
 (84, 13, 45),
 (38, 79, 51),
 (92, 45, 57),
 (46, 11, 63),
 (0, 77, 69),
 (54, 43, 75),
 (8, 9, 81),
 (62, 75, 87),
 (16, 41, 93),
 (70, 7, 99)]
'''


##################################################################
# YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest tests/test_q1.py