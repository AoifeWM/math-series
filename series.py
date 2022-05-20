import test_series


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
