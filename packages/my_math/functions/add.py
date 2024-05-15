#!/usr/bin/bash
"""code to add only two positive integers"""

from my_math.positive import is_positive

def my_add(a, b):
    if is_positive(a) and is_positive(b):
        return a + b
    return "cant perform operation on negative numbers"
