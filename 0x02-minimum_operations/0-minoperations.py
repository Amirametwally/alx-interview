#!/usr/bin/python3
"""
method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.

"""


def minOperations(n):
    ope_count = 0
    number = 2
    if type(n) is not int or n <= 1:
        return ope_count
    while n > 1:
        if n % number == 0:
            ope_count += number
            n /= number
        else:
            number += 1
    return(ope_count)