from typing import List

from test_framework import generic_test
import heapq
import bintrees
import math


class Number:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val


def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    # TODO - you fill in here.
    '''
    Note: Can be solve with min_heap but not optimal compared to BST 

    Start with 0 + 0*sqrt(2), add it to a min_heap
    Get the smallest value in min_heap, add it to res and  add 1 to a and b to get the next 2 values, add these back to min_heap
    Keep poping the smallest value from min_heap and add generate values back to min_heap till res has k element
    '''
    '''a = 0
    b = 0
    min_heap = []
    heapq.heappush(min_heap, (a+b**(1/2), a, b))
    res = []
    check = set()
    while len(res) < k:
        # print(min_heap)
        minVal, a, b = heapq.heappop(min_heap)
        if minVal not in check:
            check.add(minVal)
            res.append(minVal)
        # print(a, b)
        val1 = float(a+1 + b * math.sqrt(2))
        val2 = float(a + (b+1)*math.sqrt(2))
        # print(val1, val2)
        heapq.heappush(min_heap, (val1, a+1, b))
        heapq.heappush(min_heap, (val2, a, b+1))

    return res'''
    # Initial for 0 + 0 * sqrt(2).
    candidates = bintrees.RBTree([(Number(0, 0), None)])

    result: List[float] = []
    while len(result) < k:
        next_smallest = candidates.pop_min()[0]
        result.append(next_smallest.val)
        # Adds the next two numbers derived from next_smallest.
        candidates[Number(next_smallest.a + 1, next_smallest.b)] = None
        candidates[Number(next_smallest.a, next_smallest.b + 1)] = None
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
