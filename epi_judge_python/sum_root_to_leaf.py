from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    # TODO - you fill in here.
    '''
    Recursively find the sum from top to a leaf, sum at a node = parent node * 2 + node
    When encouter a leaf, just add it to a variable res
    Return res at the end after the recursive call
    '''
    if tree == None:
        return 0

    res = [0]
    findSum(tree, 0, res)
    return res[0]


def findSum(node, currNum, res):
    if node == None:
        return
    if node.left == None and node.right == None:
        res[0] += currNum*2 + node.data
        return

    findSum(node.left, 2*currNum + node.data, res)
    findSum(node.right, 2 * currNum + node.data, res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
