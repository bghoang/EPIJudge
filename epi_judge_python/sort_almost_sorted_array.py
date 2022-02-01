from typing import Iterator, List

from test_framework import generic_test
import heapq


def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    # TODO - you fill in here.
    '''
    Store k + 1 element in min_heap, 
    Then start poping the min element from heap and add the next element in sequence
    '''
    min_heap = []
    res = []
    #currInd = 0
    for e in sequence:
        if len(min_heap) < k+1:
            heapq.heappush(min_heap, e)
        else:
            currMin = heapq.heappushpop(min_heap, e)
            res.append(currMin)

    while min_heap:
        res.append(heapq.heappop(min_heap))
    return res


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
