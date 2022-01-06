from test_framework import generic_test


def parity(x: int) -> int:
    # TODO - you fill in here.
    counter = 0
    while x > 10:
        d = x % 10
        if d == 1:
            counter += 1
        x = x/10
    if x == 1:
        counter += 1
    if counter % 2 == 0:
        return 0
    return 1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
