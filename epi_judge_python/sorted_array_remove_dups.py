import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    # TODO - you fill in here.
    '''
    Set p1 to be 0, p2 to be 1
    Start a loop:
        If A[p1] != A[p2]: increment p1 and p2
        If A[p1] == A[p2]:
            Do a while loop, keep increment p2 till A[p2] != A[p1] or p2 == len(A)
            If p2 == len(A): then break the loop
            Else: Increment p1 to 1 and set A[p1] = A[p2]
    Return p1+1
    '''
    p1, p2 = 0, 1

    while p2 < len(A):
        if A[p1] != A[p2]:
            p1 += 1
            p2 += 1
        else:
            while p2 < len(A) and A[p1] == A[p2]:
                p2 += 1
            if p2 == len(A):
                break
            p1 += 1
            A[p1] = A[p2]

    # print(A)
    return p1+1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
