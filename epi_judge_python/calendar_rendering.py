from asyncio import events
import collections
import functools
from tokenize import endpats
from typing import List

from matplotlib.pyplot import eventplot

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))


def find_max_simultaneous_events(A: List[Event]) -> int:
    # TODO - you fill in here.
    '''
    Note: convert array from [[1,5], [2,7]] => [[1, start], [5, end], [2, start], [7, end]]. Can be done using collections.namedtuple

    Break the array into start time and event time (ex: [2,7] => [2], [7]). Then sort these times in increasing order
    Mark which one is start time, which on is end time. If the 2 times are equal, put the start time first when sorting

    Loop through this new sorted array, if encounter a start time, increase the counter by 1, else decrease the counter by 1
    Return the max counter at the end. 
    '''
    Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))

    E = ([Endpoint(event.start, True) for event in A] +
         [Endpoint(event.finish, False) for event in A])

    E.sort(key=lambda e: (e.time, not e.is_start))

    res = 0
    temp = 0

    for e in E:
        if e.is_start:
            temp += 1
            res = max(temp, res)
        else:
            temp -= 1
    return res


@enable_executor_hook
def find_max_simultaneous_events_wrapper(executor, events):
    events = [Event(*x) for x in events]
    return executor.run(functools.partial(find_max_simultaneous_events,
                                          events))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('calendar_rendering.py',
                                       'calendar_rendering.tsv',
                                       find_max_simultaneous_events_wrapper))
