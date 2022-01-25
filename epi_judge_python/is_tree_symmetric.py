from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_symmetric(tree: BinaryTreeNode) -> bool:
    # TODO - you fill in here.
    return checkSym(tree, tree)


def checkSym(node1, node2):
    if node1 == None and node2 == None:
        return True
    elif node1 == None or node2 == None:
        return False

    if node1.data != node2.data:
        return False

    firstCheck = checkSym(node1.left, node2.right)
    secondCheck = checkSym(node1.right, node2.left)

    return firstCheck and secondCheck


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
