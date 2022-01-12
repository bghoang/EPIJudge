from typing import List

from test_framework import generic_test


def fill_surrounded_regions(board: List[List[str]]) -> None:
    # TODO - you fill in here.
    '''
    Loop through the outer of the board
        If encounter a W tile, do dfs on it to get all the neighbors, mark them X as non-enclosed

    Loop through the matrix again, 
        If we encounter a W tile then we switch them to B since we know they are enclosed
        If we encounter a X tile then switch them back to W as they are non-enclosed

    DFS recusive(node, board, visited):
        if node is valid, within range of the board, else return 
        if node is visited: return
        if node == B: return
        else:
            switch node to X and explore the neighbors
    '''
    visited = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
    # print(board)
    # print(board[0:len(board)][0])
    # print(board[0:len(board)][len(board)-1])
    for i in range(len(board)):
        if board[i][0] == 'W':
            dfs(i, 0, board, visited)
            # print(board[i][0])
        if board[i][len(board[0])-1] == 'W':
            dfs(i, len(board[0])-1, board, visited)
            # print(board[i][len(board)-1])

    for j in range(len(board[0])):
        if board[0][j] == 'W':
            dfs(0, j, board, visited)
        if board[len(board)-1][j] == 'W':
            dfs(len(board)-1, j, board, visited)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                board[i][j] = 'W'
            elif board[i][j] == 'W':
                board[i][j] = 'B'

    return


def dfs(x, y, board, visited):
    if not (0 <= x < len(board) and 0 <= y < len(board[0])):
        return
    if visited[x][y] == 1:
        return
    if board[x][y] == 'B':
        return

    board[x][y] = 'X'
    visited[x][y] = 1
    if x < len(board)-1 and board[x+1][y] == "W":
        dfs(x+1, y, board, visited)
    if x > 0 and board[x-1][y] == "W":
        dfs(x-1, y, board, visited)
    if y < len(board[0])-1 and board[x][y+1] == "W":
        dfs(x, y+1, board, visited)
    if y > 0 and board[x][y-1] == "W":
        dfs(x, y-1, board, visited)

    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
