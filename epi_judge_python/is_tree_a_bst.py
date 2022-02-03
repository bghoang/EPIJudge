from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    min_val = float("-inf")
    max_val = float("inf")

    return helper(tree, min_val, max_val)


def helper(node, min_val, max_val):
    if node == None:
        return True
    if node.data > max_val or node.data < min_val:
        return False

    checkLeft = helper(node.left, min_val, node.data)
    checkRight = helper(node.right, node.data, max_val)

    return checkLeft and checkRight


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
