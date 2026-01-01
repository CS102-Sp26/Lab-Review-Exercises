import pytest
import hashlib
import os
import sys
import pprint

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import *

q1_testcases = [
    # Visible Testcases
    ((99, 0), (7, 7), 'Player 0 wins.', [(99, 0)], True), 
    ((0, 1), (7, 7), 'Player 1 wins.', [(0, 1), (7, 8), (14, 15), (21, 22), (28, 29), (35, 36), (42, 43), (49, 50), (56, 57), (63, 64), (70, 71), (77, 78), (84, 85), (91, 92), (98, 99)], True), 
    ((3, 15), (12, 18), 'Player 0 wins.', [(3, 15), (15, 33), (27, 51), (39, 69), (51, 87), (63, 5), (75, 23), (87, 41), (99, 59)], True), 
    ((32, 23, 79), (7, 11, 97), 'Player 1 wins.', [(32, 23, 79), (39, 34, 76), (46, 45, 73), (53, 56, 70), (60, 67, 67), (67, 78, 64), (74, 89, 61), (81, 0, 58), (88, 11, 55), (95, 22, 52), (2, 33, 49), (9, 44, 46), (16, 55, 43), (23, 66, 40), (30, 77, 37), (37, 88, 34), (44, 99, 31)], True), 
    ((30, 47, 39), (54, 66, 6), 'Player 2 wins.', [(30, 47, 39), (84, 13, 45), (38, 79, 51), (92, 45, 57), (46, 11, 63), (0, 77, 69), (54, 43, 75), (8, 9, 81), (62, 75, 87), (16, 41, 93), (70, 7, 99)], True), 

    # Hidden Testcases
    ((0, 1), (23, 23), 'bbd34fa4c47b91918a05b786c96ab1a7b410ad08abf0a3d737c8ee017eea6d94', '90eaff362a7204c52942b171a01d27bd08a9365bdafaea62a4a74744a74256b7', False), 
    ((14, 15), (23, 23), '063ec3f50724b9d6efd156cf20fde16c4fa253c010f0490efec5c07bfc7016b5', '8716bc650e6656ebf7fda81d28794ec1e31bea7a9b37b6c49b86ada4aeb45574', False), 
    ((12, 13), (17, 27), 'bbd34fa4c47b91918a05b786c96ab1a7b410ad08abf0a3d737c8ee017eea6d94', '0526f24b26bfa6d24249a0aa8ed4f56662a20315c3ad0eff599df481fc7c66ac', False), 
    ((53, 94, 5), (82, 67, 16), 'bbd34fa4c47b91918a05b786c96ab1a7b410ad08abf0a3d737c8ee017eea6d94', 'cc5975eaa07978fa31a017a96e671d88e4ac852099debdb62724ef4e676c56e5', False), 
    ((46, 80, 63), (22, 35, 43), '882b1b7a2edc4fee19d4ad47737b8fd457dbd51fc6949ae137b24b681440301d', 'bbb52f019647ea17984c336a8d7f44a2bf18675e44295c51a197841442dfef6c', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

def xstrip(s):
    lst = s.split('\n')
    for i in range(len(lst)):
        lst[i]=lst[i].rstrip()
    return "\n".join(lst)

@pytest.mark.parametrize("standings, jumps, win_result, r_result, testcase", q1_testcases)
def test_q1(capsys, standings, jumps, win_result, r_result, testcase):
    res = spin_the_wheel(standings, jumps)
    captured, err = capsys.readouterr()
    captured=captured.strip()
    if testcase == True:
        assert xstrip(captured) == xstrip(win_result)
        assert eval(pprint.pformat(res)) == r_result
    else:
        assert hashcode(xstrip(captured)) == win_result
        assert hashcode(eval(pprint.pformat(res))) == r_result