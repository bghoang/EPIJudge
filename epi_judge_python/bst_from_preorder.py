from typing import List, Optional

from bst_node import BstNode
from test_framework import generic_test


def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    # TODO - you fill in here.
    if len(preorder_sequence) == 0:
        return

    root = BstNode(preorder_sequence[0])

    # startInd of the right sub tree
    rightInd = len(preorder_sequence)
    for i in range(len(preorder_sequence)):
        if preorder_sequence[i] > root.data:
            rightInd = i
            break

    root.left = rebuild_bst_from_preorder(preorder_sequence[1:rightInd])
    root.right = rebuild_bst_from_preorder(preorder_sequence[rightInd::])
    return root


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('bst_from_preorder.py',
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))
