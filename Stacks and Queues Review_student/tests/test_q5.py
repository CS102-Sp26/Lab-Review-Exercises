import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q5 import *

q5_testcases = [
    ('2 1 - 3 4 2 / + *', 5.0, True), 
    ('2 3 4 + * 6 -', 8, True), 
    ('3 5 -', -2, True), 
    ('6 2 *', 12, True), 
    ('2 3 + 4 2 - *', 10, True), 
    ('2 3 1 * + 9 -', -4, True), 
    ('2 3 * 1 +', 7, True), 
    
    ('10 4 /', 'b8736b999909049671d0ea075a42b308a5fbe2df1854899123fe09eb0ee9de61', False), 
    ('10 2 8 * + 3 -', '535fa30d7e25dd8a49f1536779734ec8286108d115da5045d77f3b4185d8f790', False), 
    ('10.2 8 6 - * 3 / 112.5 +', 'd638a06aff48370b749a10650e2f08faa2fda7911277dbb9e23f4aa602d8a88f', False), 
    ('2 2 * 4 4 * + 4 /', 'a19a1584344c1f3783bff51524a5a4b86f2cc09356c9dbfb6af9cd236e314362', False), 
    ('4 2 +', 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683', False), 
    ('4 2 -', 'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35', False), 
    ('4 3 * 5 +', '4523540f1504cd17100c4835e85b7eefd49911580f8efff0599a8f283be6b9e3', False), 
    ('4 3 + 5 *', '9f14025af0065b30e47e23ebb3b491d39ae8ed17d33739e5ff3827ffb3634953', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("exp, result, testcase", q5_testcases)
def test_q5(exp, result, testcase):
    if testcase == True:
        assert postfixEval(exp) == result
    else:
        assert hashcode(postfixEval(exp)) == result