from turtle import back
from typing import List
#from warnings import _catch_warnings_with_records

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    # TODO - you fill in here.
    '''
    Main Idea: backtracking, start placing the queen at a row. For a row, check every col, if the row and col are intercepting with other queen then skip, else add them to visited and explore other rows and cols

    Workflow: 
    Keep track of the cols the positive diagnol and the negative diagnol of the location that we place the queen
    positive diagnol is where all r+c are equal
    negative diagnol is where all r-c are equal

    We going to choose a row to place the queen
    If the current row == n: then we know that all the queens are place, so just add the row and col value to result
    For each row, we loop through its col:
        if we haven't visited this col before or the row and col are not in positive diagnol nor negative diagnol
            We then updated our visited set and backtrack to the next row
    '''
    res = []
    cols_placement = [0] * n
    cols = set()
    posDig = set()
    negDig = set()

    backtrack(0, cols, posDig, negDig, n, res, cols_placement)
    return res


def backtrack(currRow, cols, posDig, negDig, n, res, cols_placement):
    if currRow == n:
        res.append(list(cols_placement))
        return
    # For each row, loop through its cols
    for col in range(0, n):
        if col in cols or (currRow + col) in posDig or (currRow-col) in negDig:
            continue
        else:
            # Updating cols_placement
            cols_placement[currRow] = col
            cols.add(col)
            posDig.add(currRow+col)
            negDig.add(currRow-col)
            backtrack(currRow+1, cols, posDig, negDig, n, res, cols_placement)

            # Remove the visited after the recusive stack ended
            cols_placement[currRow] = 0
            cols.remove(col)
            posDig.remove(currRow+col)
            negDig.remove(currRow-col)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
