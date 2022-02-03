from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils
import heapq


def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    # TODO - you fill in here.
    '''
    Use a min_heap to keep track of the k largest elements, just search through the tree 
    '''
    minheap = []

    helper(tree, k, minheap)
    return minheap


def helper(node, k, minheap):
    if node == None:
        return

    if len(minheap) < k:
        heapq.heappush(minheap, node.data)
        #helper(node.right, k, minheap)

    elif len(minheap) == k:
        if node.data > minheap[0]:
            heapq.heappushpop(minheap, node.data)

    helper(node.right, k, minheap)
    helper(node.left, k, minheap)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
