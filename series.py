import test_series

# The steps are off by one for some reason (curr actually describing the next in the series, not the "current",
# and prev being the correct output) but as far as I can tell this is just a weird semantic difference and these all
# work as expected.


def fibonacci(n):
    prev = 0
    curr = 1
    x = 0
    if isinstance(n, int) and n >= 0:
        for i in range(n):
            x = curr + prev
            prev = curr
            curr = x
        return prev
    else:
        return False


def lucas(n):
    prev = 2
    curr = 1
    x = 0
    if isinstance(n, int) and n >= 0:
        for i in range(n):
            x = curr + prev
            prev = curr
            curr = x
        return prev
    else:
        return False


def sum_series(n, prev=0, curr=1):
    x = 0
    if isinstance(n, int) and n >= 0:
        for i in range(n):
            x = curr + prev
            prev = curr
            curr = x
        return prev
    else:
        return False


test_series.fib_test(fibonacci)
test_series.lucas_test(lucas)
test_series.sum_series_test(sum_series)
