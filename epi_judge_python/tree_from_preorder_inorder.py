from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    # TODO - you fill in here.
    '''
    Use preorder list to get the root, then find index of this root in inorder list
    Use the index of the root to split the inorder list into 2 parts 
    By spliting the inorder list, we know how many nodes are in left and right subtree
    Update the preorder list and inorder list by all the information above
    Recursively build the tree from there
    '''
    return formBinaryTree(preorder, inorder, 0, len(preorder), 0, len(inorder))


def formBinaryTree(preorder, inorder, startPre, endPred, startIn, endIn):
    if startPre >= endPred:
        return None
    if startIn >= endIn:
        return None

    root = BinaryTreeNode(preorder[startPre])
    m = inorder.index(preorder[startPre])

    leftTreeSize = m - startIn
    root.left = formBinaryTree(
        preorder, inorder, startPre + 1, startPre + 1 + leftTreeSize, startIn, m)
    root.right = formBinaryTree(
        preorder, inorder, startPre + 1 + leftTreeSize, endPred, m+1, endIn)

    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
