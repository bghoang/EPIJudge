from typing import List

from test_framework import generic_test, test_utils


def generate_power_set(input_set: List[int]) -> List[List[int]]:
    # TODO - you fill in here.
    if len(input_set) == 0:
        return [[]]
    res = []
    backtrack(0, [], res, input_set)

    return res


def backtrack(currInd, currSet, res, input_set):
    if len(currSet) <= len(input_set):
        res.append(currSet)
    else:
        return
    # print(currSet)

    for i in range(currInd, len(input_set)):
        backtrack(i+1, currSet + [input_set[i]], res, input_set)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('power_set.py', 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
