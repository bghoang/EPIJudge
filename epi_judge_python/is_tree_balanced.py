from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    check = [True]
    height(tree, check)
    return check[0]


def height(node, check):
    if node == None or check[0] == False:
        return 0

    heightL = height(node.left, check)
    heightR = height(node.right, check)

    if abs(heightR-heightL) > 1:
        check[0] = False
    return max(heightL, heightR) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
