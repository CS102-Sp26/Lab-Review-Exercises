import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q1 import string_reversal

q1_testcases = [
    # Visible Testcases
    ('Alive is awesome', 'emosewa si evilA', True), 
    ('Hello World!!', '!!dlroW olleH', True), 
    ('Data structures', 'serutcurts ataD', True), 
    ('Be in present', 'tneserp ni eB', True), 
    ('hello', 'olleh', True), 
    ('Howdy', 'ydwoH', True), 
    ('', '', True), 
    ('a', 'a', True), 

    # Hidden Testcases
    ('Greetings from Earth', '421e43275ff5891156d24d6193efd3fcb3484aea3865275d9a25a5a401653b0e', False), 
    ('Greetings  from Earth', 'fd0e54fb642def356af7806c4d1902c1c855e24f18f9166bd19535902e571a7b', False), 
    ('abc123', '6ffb1ba81f30df5649bfcf654503cf4fa0f14b48d2085bc620889cfe8f031ec1', False), 
    ('123 abc', '1a0b92b6d944e489dfa2b2719c8f51a0bda20d7204e34d56e215b8b99bc642de', False), 
    ('a%bc#123$', '1cf656f8f852e8308081e221df47d2daea9ae0d13ac1fc3ca4ca9fd82c393bd2', False), 
    ('sagas', '0402594e5f30e9aebaa8b9c7febbd215eaf622184a52311e418ea07a1f9121bf', False), 
    ('My gym', '481acc0008962488de22bc2ebbdba79c606cf2a8fd74c614e135d07d72bbcedf', False), 
    ('!$!$@@', 'dc8de04ced43a328695c8164389b41e6834c3b4c1a627877482248dd9373cb0a', False), 
    ('HELLO', 'cd9f0fc13d04c4a822484b622c21ec6e7364a7f9fd949ffa5a8dd437191f10a7', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("s, result, testcase", q1_testcases)
def test_q1(s, result, testcase):
    if testcase == True:
        assert string_reversal(s) == result
    else:
        assert hashcode(string_reversal(s)) == result