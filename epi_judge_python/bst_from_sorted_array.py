import functools
from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import (binary_tree_height,
                                              generate_inorder)
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def build_min_height_bst_from_sorted_array(A: List[int]) -> Optional[BstNode]:
    # TODO - you fill in here.
    if len(A) == 0:
        return
    # print(A)
    mid = len(A)//2
    root = BstNode(A[mid])

    root.left = build_min_height_bst_from_sorted_array(A[0:mid])
    if len(A)/2 == 0:
        root.right = build_min_height_bst_from_sorted_array(A[mid:len(A)])
    else:
        root.right = build_min_height_bst_from_sorted_array(A[mid+1:len(A)])

    return root


@enable_executor_hook
def build_min_height_bst_from_sorted_array_wrapper(executor, A):
    result = executor.run(
        functools.partial(build_min_height_bst_from_sorted_array, A))

    if generate_inorder(result) != A:
        raise TestFailure('Result binary tree mismatches input array')
    return binary_tree_height(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'bst_from_sorted_array.py', 'bst_from_sorted_array.tsv',
            build_min_height_bst_from_sorted_array_wrapper))
