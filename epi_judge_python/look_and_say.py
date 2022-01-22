from test_framework import generic_test


def look_and_say(n: int) -> str:
    # TODO - you fill in here.
    '''

    set p1 and p2 and c to be 0
    create temp = []
    for each element in res
        increase p1 till res[p1] != res[p2], increment c along the way
        if res[p1] != res[p2], add c and res[p2] to temp, set p2 = p1 and reset c 
    '''
    if n == 1:
        return "1"
    res = [1]
    while n > 1:
        temp = []
        p1, p2, c = 0, 0, 0
        while p1 < len(res):
            if res[p1] == res[p2]:
                p1 += 1
                c += 1
            elif res[p1] != res[p2]:
                temp.append(c)
                temp.append(res[p2])
                p2 = p1
                c = 0
        temp.append(c)
        temp.append(res[p2])
        res = list(temp)
        n -= 1
    # print(res)
    return "".join(str(e) for e in res)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
