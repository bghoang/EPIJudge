import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    # TODO - you fill in here.
    '''
    This is checking if a graph is bipartie, meaning that for a graph, split the vertices into 2 sets
    there is no connection between 2 verices that are in the same set, only connection between 2 nodes from different sets

    Using BFS approach, keep track of the distance from each node to its neighbor
    We stop and return False if we encounter a neighbor node that has the same distance as the current node 

    Another way of doing this is to assign each node to a color, while doing bfs, if we encounter neighbor node with the same color as the current node then we return false

    '''

    for v in graph:
        if v.d == -1:
            check = bfs(v)
            if check == False:
                return False
    return True


def bfs(node):
    q = []
    q.append(node)

    while len(q) > 0:
        currNode = q.pop(0)

        for neighbor in currNode.edges:
            if neighbor.d == -1:  # If this neighbor is not visited yet
                neighbor.d = currNode.d + 1
                q.append(neighbor)
            elif neighbor.d == currNode.d:
                return False
    return True


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_circuit_wirable.py',
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
