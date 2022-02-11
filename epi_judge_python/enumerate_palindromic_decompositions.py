from turtle import back
from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    # TODO - you fill in here.
    '''
    example: 0204451881

    Recursively cut the string into parts, DON'T store the current string for recursive call, instead just partion the string from the input => (temp = text[currInd:i+1])
    Start with 0, since 0 is a palimdrom, save it and recursively check palimdrom on the rest of the string (204451881)
    If a string is not palimdrom, like 02, then we return instead of checrecursively check palimdrom on the rest of the string (04451881)
    Once the rest of the string reach 0, we add all the palimdromic decomposition into res


    '''

    res = []
    currDec = []
    backtrack(0, currDec, text, res)
    return res


def backtrack(currInd, currDec, text, res):

    if currInd == len(text):
        res.append(currDec)
        return

    for i in range(currInd, len(text)):
        temp = text[currInd:i+1]

        if temp == temp[::-1]:
            backtrack(i+1, currDec + [temp], text, res)


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'enumerate_palindromic_decompositions.py',
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
