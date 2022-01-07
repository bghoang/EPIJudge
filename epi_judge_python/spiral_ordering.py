from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    t, l = 0, 0
    b, r = len(square_matrix), len(square_matrix)
    res = []

    while True:
        for i in range(l, r):
            res.append(square_matrix[t][i])
        t += 1
        if l == r or t == b:
            break

        for i in range(t, b):
            res.append(square_matrix[i][r-1])
        r -= 1
        if l == r or t == b:
            break

        for i in range(r-1, l-1, -1):
            res.append(square_matrix[b-1][i])
        b -= 1
        if l == r or t == b:
            break

        for i in range(b-1, t-1, -1):
            res.append(square_matrix[i][l])
        l += 1
        if l == r or t == b:
            break

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
