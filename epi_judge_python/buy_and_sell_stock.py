from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # TODO - you fill in here.
    minVal = prices[0]
    maxProf = 0
    for price in prices:
        if price < minVal:
            minVal = price
        else:
            maxProf = max(maxProf, price - minVal)
    return maxProf


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
