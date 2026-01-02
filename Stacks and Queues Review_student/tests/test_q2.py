import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    (['a', 'b', 'c'], ['a', 'b', 'c', 'c', 'b', 'a'], True), 
    (['PFun', 'DSA', 'OOP'], ['PFun', 'DSA', 'OOP', 'OOP', 'DSA', 'PFun'], True), 

    # Hidden Testcases
    ([1, 2, 3], '039c8801d358724fbf3b34e5a2d51bd25cf25a4ac18530f3fcbffdb6affac110', False), 
    ([2, 'a', False], 'beb3993356180c51e1d2614a830d8a256863b9b23abeb91117320da4dd1857f5', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("queue, result, testcase", q2_testcases)
def test_q2(queue, result, testcase):
    if testcase == True:
        assert mirror(queue) == result
    else:
        assert hashcode(mirror(queue)) == result