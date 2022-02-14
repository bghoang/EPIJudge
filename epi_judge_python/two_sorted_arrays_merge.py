from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    # TODO - you fill in here.
    endPoint = m + n - 1
    p1 = m-1
    p2 = n-1

    while endPoint >= 0 and p1 >= 0 and p2 >= 0:
        if A[p1] > B[p2]:
            A[endPoint] = A[p1]
            p1 -= 1
        else:
            A[endPoint] = B[p2]
            p2 -= 1
        endPoint -= 1

    while p1 >= 0 and endPoint >= 0:
        A[endPoint] = A[p1]
        endPoint -= 1
        p1 -= 1

    while p2 >= 0 and endPoint >= 0:
        A[endPoint] = B[p2]
        endPoint -= 1
        p2 -= 1
    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
