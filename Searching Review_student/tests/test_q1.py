import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # Visible Testcases
    ([[(2, 4), (4, 6)], [(1, 2), (4, 6)], [(4, 0), (6, 6)]], 5.0, 1, True), 
    ([[(2, 4), (4, 6)], [(1, 2), (4, 6)], [(4, 0), (6, 6)]], 6.32, 2, True), 
    ([[(2, 4), (4, 6)], [(1, 2), (4, 6)], [(4, 0), (6, 6)]], 1.0, -1, True), 

    # Hidden Testcases
    ([[(2, 4), (4, 6)], [(1, 2), (4, 6)], [(4, 0), (6, 6)]], 2.83, '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("points_lists, length, result, testcase", q1_testcases)
def test_q1(points_lists, length, result, testcase):
    if testcase == True:
        assert length_of_line(points_lists, length) == result
    else:
        assert hashcode(length_of_line(points_lists, length)) == result