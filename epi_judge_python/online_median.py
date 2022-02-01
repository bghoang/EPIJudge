from typing import Iterator, List

from test_framework import generic_test
import heapq


def online_median(sequence: Iterator[int]) -> List[float]:
    # TODO - you fill in here.
    '''
    Main idea: keep max heap for smaller half and min heap for bigger half of the list, min heap > max heap by 1 always

    When new element added, we add it to min heap, then remove the min element in min heap and add it to max heap
    After that, it min heap < max heap then we add max element of max heap in min heap so that min heap always > max heap
    If min heap == max heap, Median = (min of bigger half + max of smaller half) /2
    Else, median = min of min_heap
    '''

    min_heap = []  # Bigger half
    max_heap = []  # Smaller half
    res = []

    for e in sequence:
        heapq.heappush(min_heap, e)
        currMin = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -currMin)

        # Balance the heaps
        if len(max_heap) > len(min_heap):
            currMax = heapq.heappop(max_heap)
            heapq.heappush(min_heap, -currMax)

        if len(max_heap) == len(min_heap):
            median = 0.5 * (min_heap[0] + -max_heap[0])
            res.append(median)
        else:
            res.append(min_heap[0])

    return res


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
