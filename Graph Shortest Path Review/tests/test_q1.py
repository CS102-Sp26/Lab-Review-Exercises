import hashlib
import pytest
from q1 import *

q1_testcases  = [
    ({1: [(2, 60), (4, 120)], 2: [(1, 60), (3, 80)], 3: [(5, 70), (2, 80)], 4: [(1, 120), (5, 150)], 5: [(3, 70), (4, 150)]}
    , 80, True),

    ({1: [(2, 30), (3, 70)], 2: [(1, 30), (3, 50)], 3: [(2, 50), (4, 70), (1, 70), (5, 85)], 4: [(3, 70), (5, 90)], 5: [(4, 90), (3, 85)]}
    , "b4944c6ff08dc6f43da2e9c824669b7d927dd1fa976fadc7b456881f51bf5ccc", False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()


@pytest.mark.parametrize("G, result, testcase",q1_testcases)
def test_q1(G, result, testcase):
    if testcase == True:
        assert cost_wonderland(G) == result
    else:
        assert hashcode(cost_wonderland(G)) == result