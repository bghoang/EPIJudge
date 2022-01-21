import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
def reverse_words(s):
    # TODO - you fill in here.
    # print(s)
    newS = "".join(s)
    newS = newS.split(" ")

    l = 0
    r = len(newS) - 1
    while l < r:
        newS[l], newS[r] = newS[r], newS[l]
        l += 1
        r -= 1
    newS = " ".join(newS)
    newS = list(newS)

    for i in range(len(s)):
        s[i] = newS[i]
    return


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return ''.join(s_copy)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_words.py', 'reverse_words.tsv',
                                       reverse_words_wrapper))
