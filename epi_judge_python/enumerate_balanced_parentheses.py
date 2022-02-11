from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.
    res = []
    backtrack(0, 0, num_pairs, "", res)
    return res


def backtrack(open, close, num_pairs, currStr, res):
    if open == close and open == num_pairs:
        res.append(currStr)
        return

    if open < num_pairs:
        backtrack(open + 1, close, num_pairs, currStr + "(", res)
    if close < open and close < num_pairs:
        backtrack(open, close + 1, num_pairs, currStr + ")", res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
