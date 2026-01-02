import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases =[
    ([[5, 8, 1], [6, 7, 3], [5, 4, 9]], [[1, 5, 8], [3, 6, 7], [4, 5, 9]], True), 
    ([['chair', 'table', 'house'], ['square', 'rectangle', 'triangle'], ['motor cycle', 'car', 'truck']], [['chair', 'house', 'table'], ['rectangle', 'square', 'triangle'], ['car', 'motor cycle', 'truck']], True), 
    ([[75, 28, 12], [63, 37, 23], [84, 15, 49]], [[12, 28, 75], [23, 37, 63], [15, 49, 84]], True), 
    
    ([[77, 11, 22, 3], [11, 89, 1, 12], [32, 11, 56, 7], [11, 22, 44, 33]], 'c3fe1c8fc3fd33595c544435bd80d46fc98858d331e9c64acfa556ee57b17621', False), 
    ([[8, 6, 4, 5], [3, 5, 2, 1], [9, 7, 4, 2], [7, 8, 9, 5]], '3fc569f25af660a70bb39224f8345fb5aa72f50f9a028c89a85d41b0d7e30888', False), 
    ([[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]], 'b81b776be0e575adede12f039626f1e7551efd8791a202f53bf3a8dea8c0b173', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst, result, testcase", q1_testcases)
def test_q1(lst, result, testcase):
    if testcase == True:
        assert sort_matrix_by_row(lst) == result
    else:
        assert hashcode(sort_matrix_by_row(lst)) == result