import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    # TODO - you fill in here.
    '''
    Move top n-1 disk to buffered tower
    Then move the nth disk to the destination tower
    Then move the n-1 disks from buffered tower to the destination tower 

    Note: Weird
    '''
    res = []
    # Create pegs lists
    #pegs = [[] for _ in range(NUM_PEGS)]
    #pegs[0] = [x for x in reversed(range(1, num_rings+1))]

    compute(num_rings, 0, 1, 2, res)
    return res


def compute(num_rings, from_peg, to_peg, used_peg, res):
    if num_rings > 0:

        # Move top n-1 disks from original peg to buffered pegs
        compute(num_rings-1, from_peg, used_peg, to_peg, res)

        # After moving n-1 disks, now we can move top disk of original peg to destination peg
        #topDisk = pegs[from_peg].pop()
        # pegs[to_peg].append(topDisk)
        res.append([from_peg, to_peg])

        # Move top n-1 from buffered pegs to the desination peg
        compute(num_rings-1, used_peg, to_peg, from_peg, res)


@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
