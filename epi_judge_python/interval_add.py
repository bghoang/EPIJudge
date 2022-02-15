import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    # TODO - you fill in here.
    '''
    Only merge when a[right] > b[left]
    If a[right] > b[left] and a[right] <= b[right], then use b[right]
    If a[right > b[left] and a[right] > b[right], then use a[right]
    '''
    '''disjoint_intervals.append(new_interval)
    disjoint_intervals.sort(key=lambda e: e.left)
    res = []
    if len(disjoint_intervals) == 0:
        return []

    res.append(disjoint_intervals[0])
    # print(disjoint_intervals)
    i, j = 1, 0

    while i < len(disjoint_intervals):
        b = disjoint_intervals[i]
        a = res[j]
        if a[1] >= b[0] and a[1] <= b[1]:
            temp = res[j]
            res[j] = Interval(temp[0], b[1])
        elif a[1] >= b[0] and a[1] > b[1]:
            i += 1
            continue
        else:
            res.append(b)
            j += 1
        i += 1
    return res'''

    res = []
    if len(disjoint_intervals) == 0:
        return res
    i = 0

    while i < len(disjoint_intervals):
        a = new_interval
        b = disjoint_intervals[i]

        # for the case where new_inverval[0] is less than all the left valud of the disjoint_intervals
        if a[0] <= b[0]:
            break
        # For other case
        elif b[1] >= a[0]:
            # res.append(a)
            break
        res.append(b)
        i += 1

    while i < len(disjoint_intervals):
        a = new_interval
        b = disjoint_intervals[i]
        if a[1] >= b[0]:
            left = min(a[0], b[0])
            right = max(a[1], b[1])
            new_interval = Interval(left, right)
        else:
            break
        i += 1

    return res + [new_interval] + disjoint_intervals[i::]


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
