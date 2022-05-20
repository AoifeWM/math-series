# Tests for fibonacci

def fib_test(func):
    print("Running Fibonacci tests.")

    print("Running test 1:")
    try:
        assert func(6) == 8
        print("Test 1 passed.")
    except AssertionError as E:
        print("!Test 1 failed!")

    print("Running test 2:")
    try:
        assert func(0) == 0
        print("Test 2 passed.")
    except AssertionError as E:
        print("!Test 2 failed!")

    print("Running test 3:")
    # Sanity check: program should return false if invalid input is given
    try:
        assert not func(-1)
        print("Test 3 passed.")
    except AssertionError as E:
        print("!Test 3 failed!")


def lucas_test(func):
    print("Running Lucas tests.")

    print("Running test 1:")
    try:
        assert func(3) == 4
        print("Test 1 passed.")
    except AssertionError as E:
        print("!Test 1 failed!")

    print("Running test 2:")
    try:
        assert func(7) == 29
        print("Test 2 passed.")
    except AssertionError as E:
        print("!Test 2 failed!")

    print("Running test 3:")
    # Sanity check: program should return false if invalid input is given
    try:
        assert not func("h")
        print("Test 3 passed.")
    except AssertionError as E:
        print("!Test 3 failed!")


def sum_series_test(func):
    print("Running Sum Series tests.")

    print("Running test 1:")
    # Should default to fibonacci if only one argument given
    try:
        assert func(5) == 5
        print("Test 1 passed.")
    except AssertionError as E:
        print("!Test 1 failed!")

    print("Running test 2:")
    try:
        assert func(3, 2, 3) == 8
        print("Test 2 passed.")
    except AssertionError as E:
        print("!Test 2 failed!")

    print("Running test 3:")
    # A (0, 0) series should always return 0 no matter the step
    try:
        assert func(33, 0, 0) == 0
        print("Test 3 passed.")
    except AssertionError as E:
        print("!Test 3 failed!")


