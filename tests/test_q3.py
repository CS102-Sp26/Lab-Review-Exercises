import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q3 import *

q3_testcases = [
    # Visible Testcases
    ([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 17, (5, 8), True), 
    ([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 34, -1, True), 
    ([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 19, (9, 9), True), 

    # Hidden Testcases
    ([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 42, '1bf3e274c1cf25d35274c14f962a88e3ff3eaa023617a362c7a36aba89217009', False), 
    ([0, 0, 0, 0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 0, '1f1868f06925b61765ed3f845bb2c9d04e2dc1ae4356b7495dcae6bc18ed7150', False), 
    ([0, 1, 2, 8, 13, 17, 17, 17, 17, 19, 32, 42], 3, '1bad6b8cf97131fceab8543e81f7757195fbb1d36b376ee994ad1cf17699c464', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("lst, item, result, testcase", q3_testcases)
def test_q3(lst, item, result, testcase):
    if testcase == True:
        assert find_first_and_last(lst, item) == result
    else:
        assert hashcode(find_first_and_last(lst, item)) == result