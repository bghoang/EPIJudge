from typing import List

from test_framework import generic_test, test_utils


def permutations(A: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    '''
    Backtracking with recursion, if a number is in current permutation then skip, else add it to permutation
    If permutation len is equal to len of given list and add to result. 
    '''
    res = []
    backtrack(res, [], A)
    return res


def backtrack(res, currPer, A):
    if len(currPer) == len(A):
        res.append(currPer)
        return

    for i in range(len(A)):
        if A[i] not in currPer:
            backtrack(res, currPer + [A[i]], A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('permutations.py', 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
