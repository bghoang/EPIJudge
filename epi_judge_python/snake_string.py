from test_framework import generic_test


def snake_string(s: str) -> str:
    # TODO - you fill in here.

    res = ""
    for i in range(1, len(s), 4):
        res += s[i]

    for i in range(0, len(s), 2):
        res += s[i]

    if len(s) <= 3:
        return res

    for i in range(3, len(s), 4):
        res += s[i]

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
