from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    # TODO - you fill in here.
    res = []
    backtrack(1, [], n, k, res)
    return res


def backtrack(currNum, currRes, n, k, res):
    if len(currRes) == k:
        res.append(currRes)
        return

    for i in range(currNum, n+1):
        backtrack(i+1, currRes + [i], n, k, res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
