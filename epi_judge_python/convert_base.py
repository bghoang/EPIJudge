from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    d = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    d1 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    res = ""
    temp = 0
    base = 1
    end = -1
    neg = 0
    if num_as_string[0] == '-':
        end = 0
        neg = 1
    for i in range(len(num_as_string)-1, end, -1):
        if num_as_string[i] in d1:
            digit = int(d1[num_as_string[i]]) * base
        else:
            digit = int(num_as_string[i]) * base
        temp += digit
        base *= b1

    while True:
        rem = temp % b2
        temp = temp//b2

        if rem in d:
            res += d[rem]
        else:
            res += str(rem)

        # Breakd if temp get to 0
        if temp == 0:
            break

    if neg:
        return '-' + res[::-1]
    return res[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
