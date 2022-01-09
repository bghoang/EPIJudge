from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    # TODO - you fill in here.

    # Checking each row for duplicate
    for i in range(9):
        d = dict()
        for j in range(9):
            if partial_assignment[i][j] != 0:
                if partial_assignment[i][j] in d:
                    return False
                d[partial_assignment[i][j]] = 1

    # Checking each columns for duplicate
    for i in range(9):
        d = dict()
        for j in range(9):
            if partial_assignment[j][i] != 0:
                if partial_assignment[j][i] in d:
                    return False
                d[partial_assignment[j][i]] = 1

    # Checking each 3x3 matrix
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            d = dict()
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if partial_assignment[x][y] != 0:
                        if partial_assignment[x][y] in d:
                            return False
                        d[partial_assignment[x][y]] = 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
