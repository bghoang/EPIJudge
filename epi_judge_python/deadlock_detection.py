import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    white, gray, black = range(3)

    def __init__(self) -> None:
        self.color = GraphVertex.white
        self.edges: List['GraphVertex'] = []


def is_deadlocked(graph: List[GraphVertex]) -> bool:
    # TODO - you fill in here.
    '''
    Create a visited and dfs visited list
    Loop through all the nodes, check if the node is visited, if not then call dfs on it

    dfs (node, visited, dfsVisited, graph):
        Add node into visited and dfsVisited

        for neighbor of node in graph:
            if neighbor in dfsVisited:
                return True
            elif neighbor not in visited:
                temp = dfs(neighbor, visited, dfsVisite, graph)
                if temp == True: return True because there is a cycle

        If after checking all neighbor and no cycle detect, remove node from dfsVisited and return False

    For the solution of this problem, we dont use visited and dfsVisited
    We mark each vertex as white from the begining, do similar process dfs like above, if we visited a node, mark it gray
    There is a cycle if we detect a gray to gray node

    '''
    for vertex in graph:
        if vertex.color == GraphVertex.white:  # Check if it is visited or not
            check = dfs(vertex)
            if check:
                return True

    return False


def dfs(node):
    if node.color == GraphVertex.gray:
        return True
    # Mark it as gray to show that we visited it before
    node.color = GraphVertex.gray

    for neighbor in node.edges:
        if neighbor.color != GraphVertex.black:  # Check if we already check this node when doing recursion
            if dfs(neighbor):
                return True
    # Mark it as black since we already visited all it and all its neighbor and detect no cycle
    node.color = GraphVertex.black
    return False


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('deadlock_detection.py',
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
