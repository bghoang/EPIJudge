from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    # TODO - you fill in here.
    d = {}
    for i in range(len(A)):
        d[A[i]] = perm[i]

    for k, v in d.items():
        A[v] = k
    '''
    for i in range(len(A)):
        newInd = perm[i]
        if newInd != -1:
            A[i], A[newInd] = A[newInd], A[i]
            perm[i] = -1
            perm[newInd] = -1'''
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
