import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:
    # TODO - you fill in here.
    '''
    For each recursion, build left subtree with k nodes, then right subtree with n-k-1 node
    '''
    res = buildTree(num_nodes)
    return res


def buildTree(num_nodes):
    if (num_nodes == 0):
        return [None]

    res = []
    for num_left in range(num_nodes):
        num_right = num_nodes - 1 - num_left

        leftTree = buildTree(num_left)
        rightTree = buildTree(num_right)

        res += [BinaryTreeNode(0, left, right)
                for left in leftTree for right in rightTree]
    return res


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
