from typing import List

from test_framework import generic_test


def h_index(citations: List[int]) -> int:
    # TODO - you fill in here.
    citations.sort()
    res = len(citations)
    for e in citations:
        if e >= res:
            break
        res -= 1

    return res


if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
