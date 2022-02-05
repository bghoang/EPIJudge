import functools

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(possible_anc_or_desc_0: BstNode,
                                               possible_anc_or_desc_1: BstNode,
                                               middle: BstNode) -> bool:
    # TODO - you fill in here.
    check1 = [False, False]
    check2 = [False, False]

    res1 = helper(possible_anc_or_desc_0, middle,
                  possible_anc_or_desc_1, check1)
    res2 = helper(possible_anc_or_desc_1, middle,
                  possible_anc_or_desc_0, check2)
    return res1 or res2


def helper(node, node1, node2, check):
    if node == None:
        return False

    # If we encouter
    if node.data == node2.data:
        check[1] = True
    elif node.data == node1.data:
        check[0] = True

    # If we encouter the middle node before the other other descendant node, then return false
    if check[1] and check[0] == False:
        return False
    if check[0] and check[1]:
        return True

    if check[0] == False and node.data > node1.data:
        return helper(node.left, node1, node2, check)
    elif check[0] == False and node.data < node1.data:
        return helper(node.right, node1, node2, check)
    else:
        checkLeft = helper(node.left, node1, node2, check)
        checkRight = helper(node.right, node1, node2, check)
        return checkLeft or checkRight


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(executor, tree,
                                                       possible_anc_or_desc_0,
                                                       possible_anc_or_desc_1,
                                                       middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'descendant_and_ancestor_in_bst.py',
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
