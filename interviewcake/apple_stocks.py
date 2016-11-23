# 1 - https://www.interviewcake.com/question/python/stock-price


def get_max_profit(stock_prices_yesterday):
    if stock_prices_yesterday is None or len(stock_prices_yesterday) < 2:
        return None
    min_element = min(stock_prices_yesterday[0], stock_prices_yesterday[1])
    biggest_gap = stock_prices_yesterday[1] - stock_prices_yesterday[0]
    for index, element in enumerate(stock_prices_yesterday[2:]):
        biggest_gap = max(biggest_gap, element - min_element)

        # Learning: Careful where you update counters; if this got updated first, a fully descending list breaks by always == 0
        min_element = min(element, min_element)
    return biggest_gap


assert get_max_profit(None) is None
assert get_max_profit([]) is None
assert get_max_profit([5]) is None

assert get_max_profit([10, 7, 5, 8, 11, 9]) == 6  # Example case
assert get_max_profit([15, 7, 5, 8, 11, 9]) == 6
assert get_max_profit([15, 5, 8]) == 3  # 3 element gap
assert get_max_profit([1, 5, -8]) == 4  # Check for first element being the min
assert get_max_profit([15, 7, 5, 3, 2, 0]) == -1  # Descending case
print 'OK'
