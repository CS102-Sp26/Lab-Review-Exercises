import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    (16, '1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000', True), 
    (50, '1 10 11 100 101 110 111 1000 1001 1010 1011 1100 1101 1110 1111 10000 10001 10010 10011 10100 10101 10110 10111 11000 11001 11010 11011 11100 11101 11110 11111 100000 100001 100010 100011 100100 100101 100110 100111 101000 101001 101010 101011 101100 101101 101110 101111 110000 110001 110010', True), 

    # Hidden Testcases
    (7, '3abe0c7fdf5df5a92b8411f3a18a9a0c35d5ace78fc993f78cb1315427c74a35', False), 
    (75, '858c610baae1e323395210c378acd0b4575cd43753858327011fc4de32e2f930', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("n, result, testcase", q3_testcases)
def test_q3(capsys, n, result, testcase):
    BinNumsUsingQueue(n)
    captured, err = capsys.readouterr()
    captured=captured.strip()
    if testcase == True:
        assert captured == result
    else:
        assert hashcode(captured) == result