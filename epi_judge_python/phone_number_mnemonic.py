from typing import List

from test_framework import generic_test, test_utils


def phone_mnemonic(phone_number: str) -> List[str]:
    # TODO - you fill in here.
    '''
    Create a dict to store mapping of number to letters
    currStr = ""
    res = []
    Loop through each number in phone_number:
        For values in d[number]:
            recursive(currIndex+1, currStr += value, d, res, phone_number)
    Return res

    recursive(currInd, currStr, d, res, phone_number)
        if len(currStr) == len(phone_number): add currStr to res and return
        loop through phone_number from currInd to end:
            For values in d[number]:
                recursive(currInd+1, currStr += value, d, res, phone_number)

    '''
    d = {"0": "0", "1": "1", "2": ["A", "B", "C"], "3": ["D", "E", "F"], "4": ["G", "H", "I"], "5": ["J", "K", "L"], "6": [
        "M", "N", "O"], "7": ["P", "Q", "R", "S"], "8": ["T", "U", "V"], "9": ["W", "X", "Y", "Z"]}

    currStr = ""
    res = set()
    for value in d[phone_number[0]]:
        helper(0, currStr + value, d, res, phone_number)

    return sorted(list(res))


def helper(currInd, currStr, d, res, phone_number):
    if len(currStr) == len(phone_number):
        if currStr not in res:
            res.add(currStr)
        return

    for value in d[phone_number[currInd+1]]:
        helper(currInd+1, currStr + value, d, res, phone_number)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
