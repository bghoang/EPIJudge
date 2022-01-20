import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    # TODO - you fill in here.
    '''
    Not optimal
    Create an empty array with size of s, called temp
    Loop through s
        if s[i] = a, then set temp[j] and temp[j+1] to d
        if s[i] = b, then skip
        else, set temp[j] = s[i]

    return j

    Optimal: 
              [a, c, d, c, a, c, a]
         i                          ^
    write_ind                    ^
    a_count  2
    curr_ind               ^    

    Create a write_ind and a_count
    Loop through s:
        If s[i] not b, set s[write_ind] = s[i] and write_ind+=1
        If s[i] is a, a_count+=1

    After this for loop, all the b will be removed from s and write_ind is basically just len of s without b
    Set curr_ind = write_ind - 1, curr_ind is basically the current index of the s after we removed all the b
    Set finalSize = write_ind + a_count since we have the length of s after removing b but we need to add extra space for the a replaced by dd
    Set write_ind += a_count - 1 because we now need to account for all the a elements in s, so the write_ind will need to be 
    changed to have more space for the a. write_ind now will be at the last index of the new array with account for additional space to replace a with dd

    Loop backward from curr_ind -> 0 on string s:
        if s[curr_ind] = a
            change s[write_ind] and s[write_ind-1] to d
            write_ind -= 2
        else: 
            s[write_ind] = s[curr_ind]
            write -= 1
        curr_ind -= 1
    return finalSize

    '''
    '''
    temp = [0] * len(s)
    i, j = 0, 0

    while i < size:
        if s[i] == 'a':
            temp[j] = 'd'
            temp[j+1] = 'd'
            j += 2
            i += 1
        elif s[i] == 'b':
            i += 1
            continue
        else:
            temp[j] = s[i]
            i += 1
            j += 1

    for i in range(j):
        s[i] = temp[i]
    return j'''

    write_ind, a_count = 0, 0
    for i in range(size):
        if s[i] != 'b':
            s[write_ind] = s[i]
            write_ind += 1
        if s[i] == 'a':
            a_count += 1

    curr_ind = write_ind - 1
    finalSize = write_ind + a_count
    write_ind += a_count - 1

    while curr_ind >= 0:
        if s[curr_ind] == 'a':
            s[write_ind] = 'd'
            s[write_ind-1] = 'd'
            write_ind -= 2
        else:
            s[write_ind] = s[curr_ind]
            write_ind -= 1
        curr_ind -= 1

    return finalSize


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
