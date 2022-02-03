from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    # TODO - you fill in here.
    if tree == None:
        return None

    if tree.data == key:
        return tree

    elif tree.data < key:
        return search_bst(tree.right, key)
    else:
        return search_bst(tree.left, key)


def search_bst_wrapper(tree, key):
    result = search_bst(tree, key)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_in_bst.py', 'search_in_bst.tsv',
                                       search_bst_wrapper))
