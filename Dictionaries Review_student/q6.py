def contacts():
    """
    Read names and phone numbers from input until 'STOP' and return
    a dictionary mapping formatted names ('Last, First(s)' or single
    names unchanged) to sorted lists of unique phone numbers.

    Returns:
        dict: Contact dictionary with sorted phone number lists.
    """

    # WRITE YOUR CODE HERE
    pass


import pprint
if __name__ == "__main__":
    #############################################################################
    # Let's test your code on visible test cases... Run your code file and      #
    # check manually whether the code is running as expected...                 #
    #############################################################################

    pprint.pprint(contacts())
    '''
    Inputs:
    Sona 0300-555-1111
    Chandi 0300-555-2222
    Chacha Karmoo 0300-333-7777
    Maasi Barkatay 0300-222-9999
    Nawab Farasat Ali Khan 0388-888-8888
    STOP

    Output:
    {'Barkatay, Maasi': ['0300-222-9999'],
    'Chandi': ['0300-555-2222'],
    'Karmoo, Chacha': ['0300-333-7777'],
    'Khan, Nawab Farasat Ali': ['0388-888-8888'],
    'Sona': ['0300-555-1111']}
    '''

    print()

    pprint.pprint(contacts())
    '''
    Inputs:
    Sona 0300-555-1111
    Sona 0300-555-1112
    Chandi 0300-555-2222
    Chandi 0300-555-2223
    Chandi 0300-555-2224
    Chacha Karmoo 0300-333-7777
    Chacha Karmoo 0300-333-7778
    Maasi Barkatay 0300-222-9999
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8889
    Nawab Farasat Ali Khan 0388-888-8898
    Nawab Farasat Ali Khan 0388-888-8899
    Nawab Farasat Ali Khan 0388-889-8888
    Nawab Farasat Ali Khan 0388-889-8889
    STOP

    Outputs:
    {'Barkatay, Maasi': ['0300-222-9999'],
    'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    'Karmoo, Chacha': ['0300-333-7777', '0300-333-7778'],
    'Khan, Nawab Farasat Ali': ['0388-888-8888',
                                '0388-888-8889',
                                '0388-888-8898',
                                '0388-888-8899',
                                '0388-889-8888',
                                '0388-889-8889'],
    'Sona': ['0300-555-1111', '0300-555-1112']}
    '''

    print()

    pprint.pprint(contacts())
    '''
    Inputs:
    Sona 0300-555-1112
    Chandi 0300-555-2224
    Chandi 0300-555-2222
    Chandi 0300-555-2223
    Sona 0300-555-1111
    STOP

    Outputs:
    {'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    'Sona': ['0300-555-1111', '0300-555-1112']}
    '''

    print()

    pprint.pprint(contacts())
    '''
    Inputs:
    Sona 0300-555-1111
    Sona 0300-555-1111
    Chandi 0300-555-2222
    Chandi 0300-555-2222
    Chandi 0300-555-2222
    Chacha Karmoo 0300-333-7777
    Chacha Karmoo 0300-333-7777
    Maasi Barkatay 0300-222-9999
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-888-8888
    STOP

    Outputs:
    {'Barkatay, Maasi': ['0300-222-9999'],
    'Chandi': ['0300-555-2222'],
    'Karmoo, Chacha': ['0300-333-7777'],
    'Khan, Nawab Farasat Ali': ['0388-888-8888'],
    'Sona': ['0300-555-1111']}
    '''
    
    print()

    pprint.pprint(contacts())
    '''
    Inputs:
    Chacha Karmoo 0300-333-7778
    Chandi 0300-555-2223
    Nawab Farasat Ali Khan 0388-888-8898
    Nawab Farasat Ali Khan 0388-888-8899
    Chandi 0300-555-2224
    Sona 0300-555-1111
    Chacha Karmoo 0300-333-7778
    Chandi 0300-555-2224
    Nawab Farasat Ali Khan 0388-888-8888
    Chandi 0300-555-2222
    Nawab Farasat Ali Khan 0388-889-8889
    Sona 0300-555-1112
    Chacha Karmoo 0300-333-7777
    Nawab Farasat Ali Khan 0388-888-8888
    Nawab Farasat Ali Khan 0388-889-8888
    Chandi 0300-555-2222
    Chandi 0300-555-2222
    Nawab Farasat Ali Khan 0388-888-8889
    Nawab Farasat Ali Khan 0388-888-8888
    Chacha Karmoo 0300-333-7778
    Maasi Barkatay 0300-222-9999
    Maasi Barkatay 0300-222-9999
    STOP

    Outputs:
    {'Barkatay, Maasi': ['0300-222-9999'],
    'Chandi': ['0300-555-2222', '0300-555-2223', '0300-555-2224'],
    'Karmoo, Chacha': ['0300-333-7777', '0300-333-7778'],
    'Khan, Nawab Farasat Ali': ['0388-888-8888',
                                '0388-888-8889',
                                '0388-888-8898',
                                '0388-888-8899',
                                '0388-889-8888',
                                '0388-889-8889'],
    'Sona': ['0300-555-1111', '0300-555-1112']}
    '''


    ##################################################################
    # YOU CAN DO FURTHER CUSTOM TESTING BELOW ....                   #
    ##################################################################


# Testing For all testcases 
# In order to test your function, type the following command on the terminal:
# pytest test_q6.py