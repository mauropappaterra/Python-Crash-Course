# Python Crash Course 
# testing.py
# Created by Mauro J. Pappaterra on 10 of October 2017.

############################################ UNIT TEST MODULE
import unittest

def myFunction (a):
    return a * 2

def testMyFunction (a):
    result = a * 2
    assert result is not None
    assert result % 2 == 0

testMyFunction(10)
