#!/usr/bin/python3

from .abs import my_abs

def is_positive(n):
    return my_abs(n) == n
