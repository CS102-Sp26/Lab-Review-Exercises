import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    ([3, 4], 20, (2, 9), True), 
    ([3, 4], 120, (1, 14), True), 
    ([5, 3], 100, (2, 23), True), 
    ([5, 7], 100, (1, 66), True), 
    ([5, 4, 3], 17, (1, 5), True), 

    # Hidden Testcases
    ([4, 6], 80, 'c91b9a4b9fc870aede88e86274bdbe45c2c40b0f76a6dd21a91a94fbd88f2ae1', False), 
    ([4, 6], 630, 'd3b4144b7e1a5ceb32c7718ea1f76c2ac6f838aa2b19c2786f7152ca461def36', False), 
    ([7, 3], 630, '76db322cc7ba5fa9cb76b4d6e5988a4e15e8a029938e1a6700aa9934b44bea14', False), 
    ([7, 10], 630, '327e886f82d06ad43419ed09ca361b02ffda4fd7e2bccea512d3b3c15955e6cd', False), 
    ([4, 6, 7], 31, 'd3deed7b73808543cf81e2562b9848485f8394e9c3065fdd5c09335b0c85b4d3', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("sides, goal, result, testcase", q2_testcases)
def test_q2(sides, goal, result, testcase):
    if testcase == True:
        assert multipillionaire(sides, goal) == result
    else:
        assert hashcode(multipillionaire(sides, goal)) == result