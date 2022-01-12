import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:
    # TODO - you fill in here.
    '''
    Create a visited array
    Create a stack
    Call recursive DFS(maze, s, e, visited, stack)
    Return stack

    RecursiveDFS(maze, currNode, e, visited, stack):
        if the currNode is not within the maze or not equal to WHITE: return False
        if currNode is in visited: return False
        add currNode to the stack
        mark currNode as visited
        if currNode == e then return True
        call RecursiveDFS on all the currNode's neighbors
        if can't find the path then remove the currNode from the stack and return False
    '''
    stack = []
    visited = [[0 for _ in range(len(maze[0]))] for _ in range(len(maze))]
    # Start DFS
    if (recursiveDFS(maze, s, e, visited, stack)):
        return stack
    return []


def recursiveDFS(maze, currNode, e, visited, stack):
    if not (currNode.x >= 0 and currNode.x < len(maze) and currNode.y >= 0 and currNode.y < len(maze[0])):
        return False
    if (maze[currNode.x][currNode.y] == BLACK or visited[currNode.x][currNode.y] == 1):
        return False

    stack.append(currNode)
    visited[currNode.x][currNode.y] = 1
    if (currNode.x == e.x and currNode.y == e.y):
        return True

    # Check neighbor
    n1 = Coordinate(currNode.x-1, currNode.y)
    n2 = Coordinate(currNode.x, currNode.y-1)
    n3 = Coordinate(currNode.x+1, currNode.y)
    n4 = Coordinate(currNode.x, currNode.y+1)

    if (recursiveDFS(maze, n1, e, visited, stack) or
        recursiveDFS(maze, n2, e, visited, stack) or
        recursiveDFS(maze, n3, e, visited, stack) or
            recursiveDFS(maze, n4, e, visited, stack)):
        return True

    stack.pop()
    return False


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
        cur == (prev.x - 1, prev.y) or \
        cur == (prev.x, prev.y + 1) or \
        cur == (prev.x, prev.y - 1)


@ enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
