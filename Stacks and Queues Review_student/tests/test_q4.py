import pytest
import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from q4 import *

q4_testcases = [
    # Visible Testcases
    ('( A + B ) * ( C + D )', '* + A B + C D', True), 
    ('A * B + C * D', '+ * A B * C D', True), 
    ('A * B + C', '+ * A B C', True), 
    ('A * ( B + C )', '* A + B C', True), 
    ('A - B', '- A B', True), 
    ('A + B * C', '+ A * B C', True), 
    ('( A + B ) * C', '* + A B C', True), 
    
    # Hidden Testcases
    ('( A + B ) * C - ( D - E ) * ( F + G )', 'd69efaba322470b8868263884e68bc6349b4dcc6f4f21a1db1e6a13480b5bc7f', False), 
    ('( ( ( A + B ) * C ) - ( ( D - E ) * ( F + G ) ) )', 'd69efaba322470b8868263884e68bc6349b4dcc6f4f21a1db1e6a13480b5bc7f', False), 
    ('( P + Q ) * ( M - N )', '3284b407e6c3a1bf74081d8933474be67b7a3b1fd2cfc367d132fe59285d2b65', False), 
    ('( P + Q ) / ( M - N ) - ( A * B )', '129e70826a20aff1e0c2f89ec386fda5e38f4e3d530454785152e18b1b21987e', False), 
    ('X + Y', 'b61f57aefab5ab6a04ca97cc163d358a94830f482bfed7e1180f374e827826e6', False), 
    ('X + Y * Z', 'e9e66e98031dbac5cc0fa162302191415a4ad60a24282caf2b536f3949d0d84a', False), 
    ('( X + Y ) * Z', 'ede0df9c7f7dd9d4f6eaaa9739a065d5dc3c6f2e797bc14a5f170d6575fe8b22', False)
]

def hashcode(n: int) -> str:
    return hashlib.sha256(str(n).encode('utf-8')).hexdigest()

@pytest.mark.parametrize("expression, result, testcase", q4_testcases)
def test_q4(expression, result, testcase):
    if testcase == True:
        assert Infix_to_Prefix(expression) == result
    else:
        assert hashcode(Infix_to_Prefix(expression)) == result