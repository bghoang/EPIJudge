from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # TODO - you fill in here.
    '''
    Have a variable to keep track of the smaller nummber bigger than k called maxVal
    Do binary search, if the current node is > k and < maxVal then maxVal = currNode
    Seach for right sub tree if k >= currNode, else search left sub tree
    '''
    if tree == None:
        return

    maxVal = [None]
    bs(tree, k, maxVal)

    return maxVal[0]


def bs(node, k, maxVal):
    if node == None:
        return

    if maxVal[0] == None and node.data > k:
        maxVal[0] = node
    elif node.data > k and node.data < maxVal[0].data:
        maxVal[0] = node

    if node.data > k:
        bs(node.left, k, maxVal)
    else:
        bs(node.right, k, maxVal)


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
