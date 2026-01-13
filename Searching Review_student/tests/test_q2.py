import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q2 import *

q2_testcases = [
    # Visible Testcases
    ([1, 3, 5, 9, 4, 1], 3, True), 
    ([1, 3, 5, 9, 4], 3, True), 
    ([10, 12, 20, 32, 37, 35, 30, 25], 4, True), 
    ([10, 12, 20, 32, 35, 30, 25], 4, True), 
    ([1, 10, 12, 15, 5, 3, 2], 3, True), 

    # Hidden Testcases
    ([50, 60, 70, 80, 40, 30, 20, 10], '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False), 
    ([-5, -3, -2, 0, 1, 2, -7, -8, -10], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False), 
    ([-3, -2, -4], '6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b', False), 
    ([8, 9, 15, 16, 20, 13, 12, 4, 2], '4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a', False), 
    ([5000, 10000, 15000, 16000, 17000, 18000, 1000, 100, 10], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False), 
    ([-1000, -500, -100, -50, -10000, -20000, -30000], '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("unimodel_sequence, result, testcase", q2_testcases)
def test_q2(unimodel_sequence, result, testcase):
    if testcase == True:
        assert getTopIndex_UnimodelSequence(unimodel_sequence) == result
    else:
        assert hashcode(getTopIndex_UnimodelSequence(unimodel_sequence)) == result