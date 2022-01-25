from signal import signal
from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    if (len(num1) == 1 and num1[0] == 0) or (len(num2) == 1 and num2[0] == 0):
        return [0]

    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    num1.reverse()
    num2.reverse()
    currInd = 0
    for i in range(len(num2)):
        currInd = i
        remainder = 0
        for j in range(len(num1)):
            temp = result[currInd] + num2[i]*num1[j] + remainder
            remainder = temp // 10
            result[currInd] = temp % 10
            currInd += 1
        if currInd < len(result):
            result[currInd] += remainder

    p1 = len(result)-1
    while result and result[p1] == 0:
        result.pop()
        p1 -= 1

    result.reverse()
    result[0] = result[0] * sign
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
