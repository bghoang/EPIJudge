from os import remove
import queue
from typing import Set
import string

from test_framework import generic_test


def transform_string(D: Set[str], s: str, t: str) -> int:
    # TODO - you fill in here.
    '''
    BFS
    NOTE: checking for only 1 differ character from string is complex. 
    Create a queue
    Add (s,0) to q: q = [(s,0)]

    while q not empty:
        Pop the top of queue to get the current node
        Get the current string in the current node
        Check if this currString == t: return currNode[1]

        Try all the combination of a random character with 2 characters from 2 string
            If this new combincation in D
                Remove this combincation in D
                Add this new combincation in D with the currNode[1]+1 to increase the distance by 1
    Return -1 

    '''
    # StringWithDistance = collections.namedtuple(
    #   'StringWithDistance', ('candidate_string', 'distance'))
    # print(StringWithDistance)
    #q = collections.deque([StringWithDistance(s, 0)])
    # print(q)
    q = [(s, 0)]

    while len(q) != 0:
        currNode = q.pop(0)
        currWord = currNode[0]

        if currWord == t:
            return currNode[1]

        for i in range(len(currWord)):
            # Loop through each character in the alphabet lowercase
            for c in string.ascii_lowercase:
                # Add this character with 2 letters from the currWord
                # Check if this new word is in D, if so then add it the queue and remove it from D
                # to reduce the search
                temp = currWord[:i] + c + currWord[i+1:]
                if temp in D:
                    D.remove(temp)
                    q.append((temp, currNode[1]+1))

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_transformability.py',
                                       'string_transformability.tsv',
                                       transform_string))
