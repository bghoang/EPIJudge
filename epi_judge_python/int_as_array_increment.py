from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    carry = 0
    A.reverse()
    for i in range(len(A)):
        # print(A[i])
        newVal = 0
        # For the first value only
        if i == 0:
            newVal = A[i] + 1
        else:
            newVal = A[i] + carry
            carry = 0

        if newVal > 9:
            A[i] = 0
            carry = 1
        else:
            A[i] = newVal

    if carry == 1:
        A.append(carry)
    A.reverse()
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
