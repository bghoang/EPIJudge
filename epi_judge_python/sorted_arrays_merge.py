import enum
from typing import List

from test_framework import generic_test
import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    '''
    Use min heap to keep track of the minimum element
    Initialize min heap to be all the first element of list in list
    Remove min element, add the next element from the list that has the min element to min heap    
    '''
    min_heap = []

    sorted_iter = [iter(x) for x in sorted_arrays]

    for i, element in enumerate(sorted_iter):
        # Add the first element of each list in sorted_iter, it no next then set None as default
        first_element = next(element, None)
        if first_element != None:
            heapq.heappush(min_heap, (first_element, i))

    res = []
    while min_heap:
        # Get the min element in heap and the list that that element is from
        min_elem, currListInd = heapq.heappop(min_heap)
        res.append(min_elem)

        # Add the next number of the list that the current min number is from to min_heap
        next_ele = next(sorted_iter[currListInd], None)
        if next_ele != None:
            heapq.heappush(min_heap, (next_ele, currListInd))

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
