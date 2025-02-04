import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    # TODO - you fill in here.
    if node1.data == node0.data:
        return node1

    h0 = getDepth(node0)
    h1 = getDepth(node1)

    if h0 < h1:
        while h0 != h1 and node1.parent != None:
            node1 = node1.parent
            h1 -= 1
    elif h0 > h1:
        while h0 != h1 and node0.parent != None:
            node0 = node0.parent
            h0 -= 1

    return findParent(node0, node1)


def getDepth(node):
    height = 0
    while node != None:
        node = node.parent
        height += 1
    return height


def findParent(node0, node1):
    if node0 == node1:
        return node1

    while node0 != None and node1 != None:
        if node0.parent == node1.parent:
            return node0.parent
        node0 = node0.parent
        node1 = node1.parent

    return None


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
