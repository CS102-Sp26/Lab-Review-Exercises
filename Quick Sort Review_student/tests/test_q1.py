import pytest
import hashlib
from sys import stderr
from q1 import *

q1_testcases  = [
    # Visible Testcases
    ([5 , 9 , 2 , 1 , 6 , 3 , 0], 0, 6, [0, 1, 2, 3, 5, 6, 9], True), 
    ([21 , 36 , 11 , 9 , 6 , 42 , 39], 0, 6, [6, 9, 11, 21, 36, 39, 42], True), 
    ([], 0, -1, [], True), 
    ([101], 0, 0, [101], True), 

    # Hidden Testcases
    (['zebra', 'ape', 'tiger', 'lion'], 0, 3, '1aa571878402a095e59c11877d12df243f1f4ffb59183868a6f6054b953f20c6', False), 
    ([99, 75, 101, 32, 67, 2, 10, 100, 0, 11, 22, 33, 77, 1, 28, 101, 20, 30, 45, 25, 43, 89], 0, 21, '5a51e46ad88881782b65b2b4a51b013f4d9bbe52a125f0ed927c6ba4c6f1a1d4', False), 
    ([-67, -33, 34, 49, 71, -94, -4, -63, -49, -36, -45, 21, 47, 96, 46, -74, -38, 56, -51, 15, -68, 35, -41, -93, 52, 9, 40, 49, 95, -93, -2, 92, 33, -50, 45, 53, 6, 0, 50, 43, 16, -4, -91, -29, -37, -90, 32, 89, -41, -38], 0, 49, '44c619046942f3d027f8e846bf96749dbfdc4a603cbbb442d35de0ffc08f5ebf', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst,low,high,result,testcase",q1_testcases)
def test_q1(capsys, lst, low, high, result, testcase):
    quick_sort(lst, low, high)
    if testcase == True:
        assert lst == result
    else:
        assert hashcode(lst) == result