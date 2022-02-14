import copy
import functools
import math
from typing import List

from matplotlib import gridspec

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def solve_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.
    slots = []
    for i in range(9):
        for j in range(9):
            if partial_assignment[i][j] == 0:
                slots.append([i, j])
    # print(slots)
    res = backtrack(0, slots, partial_assignment)
    # print(partial_assignment)
    return res


def backtrack(currInd, slots, partial_assignment):
    if currInd == len(slots):
        return True
    # print(partial_assignment)
    for i in range(9):
        currI, currJ = slots[currInd][0], slots[currInd][1]

        if isValid(currI, currJ, partial_assignment, i+1):
            partial_assignment[currI][currJ] = i+1
            if backtrack(currInd + 1, slots, partial_assignment):
                return True
            else:
                partial_assignment[currI][currJ] = 0
    return False


def isValid(currI, currJ, partial_assignment, c):
    for n in range(len(partial_assignment)):
        if partial_assignment[currI][n] == c:
            return False
        if partial_assignment[n][currJ] == c:
            return False

    gridX, gridY = 3*(currI//3), 3*(currJ//3)
    for x in range(gridX, gridX+3):
        for y in range(gridY, gridY+3):
            if partial_assignment[x][y] == c:
                return False
    return True


def assert_unique_seq(seq):
    seen = set()
    for x in seq:
        if x == 0:
            raise TestFailure('Cell left uninitialized')
        if x < 0 or x > len(seq):
            raise TestFailure('Cell value out of range')
        if x in seen:
            raise TestFailure('Duplicate value in section')
        seen.add(x)


def gather_square_block(data, block_size, n):
    block_x = (n % block_size) * block_size
    block_y = (n // block_size) * block_size

    return [
        data[block_x + i][block_y + j] for j in range(block_size)
        for i in range(block_size)
    ]


@enable_executor_hook
def solve_sudoku_wrapper(executor, partial_assignment):
    solved = copy.deepcopy(partial_assignment)

    executor.run(functools.partial(solve_sudoku, solved))

    if len(partial_assignment) != len(solved):
        raise TestFailure('Initial cell assignment has been changed')

    for (br, sr) in zip(partial_assignment, solved):
        if len(br) != len(sr):
            raise TestFailure('Initial cell assignment has been changed')
        for (bcell, scell) in zip(br, sr):
            if bcell != 0 and bcell != scell:
                raise TestFailure('Initial cell assignment has been changed')

    block_size = int(math.sqrt(len(solved)))
    for i, solved_row in enumerate(solved):
        assert_unique_seq(solved_row)
        assert_unique_seq([row[i] for row in solved])
        assert_unique_seq(gather_square_block(solved, block_size, i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sudoku_solve.py', 'sudoku_solve.tsv',
                                       solve_sudoku_wrapper))
