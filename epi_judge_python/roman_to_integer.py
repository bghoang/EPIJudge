from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # TODO - you fill in here.
    d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    if len(s) == 1:
        return d[s[0]]
    res = 0
    i = len(s)-1
    while i >= 0:
        if i < len(s)-1 and d[s[i+1]] > d[s[i]]:
            res -= d[s[i]]
        else:
            res += d[s[i]]
        i -= 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
