from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.
    '''
    Loop from the end of the list till we find a location k where perm[k] < perm[k+1]
    From location k+1 to end of list, find min(list[k+1::]) that bigger than perm[k] and its location l
    Swap perm[k] and perm[l]
    From location k+1, start sorting so that perm is in increasing order. 
    '''

    k = len(perm) - 2
    l = 0
    while k >= 0:
        #print(perm[k], perm[k+1])
        if perm[k] < perm[k+1]:
            # print(k)
            break
        k -= 1

    # print(k)
    # If perm is in decreasing order then no next permutation
    if k == -1:
        return []

    minVal = float("inf")
    minInd = 0
    for i in range(k+1, len(perm)):
        if minVal >= perm[i] and perm[i] > perm[k]:
            minVal = perm[i]
            minInd = i

    perm[k], perm[minInd] = perm[minInd], perm[k]
    perm[k+1::] = reversed(perm[k+1::])
    return perm


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
