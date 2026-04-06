import hashlib
import pytest
from q2 import *

q2_testcases  = [
    ({'a': [('b', 10), ('d', 10)], 'b': [('a', 10), ('c', 10)], 'c': [('b', 10), ('d', 10)], 'd': [('c', 10), ('a', 10)]}
    , ['b'], 'a', 'c', (0, 20), True),
    ({'a': [('b', 5), ('d', 10)], 'b': [('a', 5), ('c', 10)], 'c': [('b', 10), ('d', 10)], 'd': [('c', 10), ('a', 10)]}
    , ['b', 'd'], 'a', 'c', (1, 15), True),
    ({'a': [('b', 10), ('d', 10)], 'b': [('a', 10), ('c', 10)], 'c': [('b', 10), ('d', 8), ('e', 5)], 'd': [('c', 8), ('a', 10)], 'e': [('c', 5)]}
    , ['c'], 'a', 'e', "06ef99d90592fc4e2b71f2b7540c992ea530aef2ed2e650089f6c89b7f1b1440", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("G, cursed, start_node , end_node, result, testcase", q2_testcases)
def test_q2(G, cursed, start_node , end_node, result, testcase):
    if testcase == True:
        assert distance(G, cursed, start_node, end_node) == result
    else:
        assert hashcode(distance(G, cursed, start_node, end_node)) == result