from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    # TODO - you fill in here.
    '''
    Do BFS iteratively, the reason is because we want to check for the color of the previous point.
    Create a queue q
    Created a visited list
    Add (x,y) to the queue
    Save old color at x,y

    while q is not empty:
        Pop the first element of the queue
        Flip this color of this element
        Mark as visited
        Check the neighbor, check if they are within range 0<= x <= len(image) and 0<= y <= len(image[0])
            if any of them we haven't visited and if any of them has the same oldColor then add them to the queue        
    '''

    q = []
    visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
    q.append((x, y))
    oldColor = image[x][y]

    while len(q) != 0:
        currNode = q.pop(0)
        # print(currNode)
        #oldColor = image[currNode[0]][currNode[1]]
        # print(oldColor)
        image[currNode[0]][currNode[1]] = 1-oldColor
        visited[currNode[0]][currNode[1]] = 1

        n1 = (currNode[0]-1, currNode[1])
        n2 = (currNode[0]+1, currNode[1])
        n3 = (currNode[0], currNode[1]-1)
        n4 = (currNode[0], currNode[1]+1)
        maxR = len(image[0])
        maxB = len(image)

        if isValid(n1, maxR, maxB) and visited[n1[0]][n1[1]] == 0 and image[n1[0]][n1[1]] == oldColor:
            q.append(n1)
        if isValid(n2, maxR, maxB) and visited[n2[0]][n2[1]] == 0 and image[n2[0]][n2[1]] == oldColor:
            q.append(n2)
        if isValid(n3, maxR, maxB) and visited[n3[0]][n3[1]] == 0 and image[n3[0]][n3[1]] == oldColor:
            q.append(n3)
        if isValid(n4, maxR, maxB) and visited[n4[0]][n4[1]] == 0 and image[n4[0]][n4[1]] == oldColor:
            q.append(n4)
    return


def isValid(node, maxR, maxB):
    if (node[0] >= 0 and node[0] < maxB and node[1] >= 0 and node[1] < maxR):
        return True
    return False


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
