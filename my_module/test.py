"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.function import read_email_as_Strings, encryption, decryption
import os

def test_my_emailReader():

    assert os.listdir('text') != 0

def test_my_encryption(start_key,key_increment,message):

    assert isinstance(encryption(start_key,key_increment,message),str)
    
def test_my_decryption(start_key,key_increment,encoded):

    assert isinstance(decryption(start_key,key_increment,encoded),str)
