import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

q4_testcases = [
    # Visible Testcases
    ([4, 3, 2, 1], 5, True), 
    ([4, 3, 2], 1, True), 
    ([6, 5, 3, 2, 1], 4, True), 
    ([6, 4, 3, 2, 1], 5, True), 
    ([9, 8, 7, 6, 5, 4, 3, 1], 2, True), 
    ([9, 8, 7, 6, 5, 3, 2, 1], 4, True), 
    ([8, 7, 6, 5, 4, 3, 2, 1], 9, True), 

    # Hidden Testcases
    ([9, 8, 7, 5, 4, 3, 2, 1], 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False), 
    ([9, 8, 7, 6, 5, 4, 2, 1], '4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce', False), 
    ([9, 8, 7, 6, 5, 4, 3, 2, 1], '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5', False), 
    ([10, 9, 8, 7, 6, 4, 3, 2, 1], 'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d', False), 
    ([11, 10, 9, 8, 6, 5, 4, 3, 2, 1], '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451', False), 
    ([11, 10, 9, 7, 6, 5, 4, 3, 2, 1], '2c624232cdd221771294dfbb310aca000a0df6ac8b66b696d90ef06fdefb64a3', False), 
    ([11, 10, 9, 8, 7, 5, 4, 3, 2, 1], 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("nums, result, testcase", q4_testcases)
def test_q4(nums, result, testcase):
    if testcase == True:
        assert findMissingNumber(nums) == result
    else:
        assert hashcode(findMissingNumber(nums)) == result