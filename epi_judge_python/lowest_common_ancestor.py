import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    '''
    Main Idea for the case of node0 != node1: 
    for each recursive call:
        check if the currNode is the equal to either node1 or node0
        check if node1 or node0 in right sub tree
        check if node2 or node0 in left sub tree
        If 2 out of 3 of these conditions are True: then update LCA
        return true if 1 of 3 condition above is true

    Another solution for the case of node0 == node1:
    For each recursive call:
        If node0 or node1 is equal to the currentNode, then just return the currentNode
        Check left and right subtree
        If left is none then return right since can't find any matching nodes from left sub tree
        If right is none then return left since can't find any matching nodes from right sub tree
        Else that mean that node0 and node1 are in left and right sub tree, then just return the current node

    '''
    # TODO - you fill in here.
    if(tree == None or tree.data == node0.data or tree.data == node1.data):
        return tree
    left = lca(tree.left, node0, node1)
    right = lca(tree.right, node0, node1)

    if(left == None):
        return right
    elif right == None:
        return left
    else:
        return tree


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
