from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string


def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    res = []
    neg = 0
    if x < 0:
        neg = 1
        x = x * -1
    while True:
        lastDigit = x % 10
        res.append(chr(ord('0') + lastDigit))
        x = x//10
        if x == 0:
            break
    if neg:
        return "-" + "".join(reversed(res))
    return "".join(reversed(res))


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    res = 0
    neg = 0
    start = 0
    if s[0] == "-":
        neg = 1
        start = 1
    elif s[0] == "+":
        start = 1
    for i in range(start, len(s)):
        temp = int(s[i])
        res += temp
        if i != len(s)-1:
            res = res * 10

    if neg:
        return 0 - res
    return res
    '''
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] in '-+':], 0)'''


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
