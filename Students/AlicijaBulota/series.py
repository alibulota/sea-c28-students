#Fibonacci Series


def fibonacci(n):
    """Fibonacci series function to return
    nth value in series using recursion"""
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        return None
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#
#Lucas Numbers


def lucas(n):
    """function to find nth value for
    Lucas Numbers"""
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        return None
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

#
#sum_series


def sum_series(n, opt_par0=0, opt_par1=1):
    """function to find nth value in summed
    integer sequence"""
    if not isinstance(n, int):
        raise ValueError
    if n < 0:
        return None
    if n == 0:
        return opt_par0
    elif n == 1:
        return opt_par1
    else:
        return sum_series(n - 1, opt_par0, opt_par1) + \
            sum_series(n - 2, opt_par0, opt_par1)

if __name__ == '__main__':
    fib_vals = [  # test first 6 values of fib. series
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5)
    ]

    lucas_vals = [  # test first 6 values of lucas series
        (0, 2),
        (1, 1),
        (2, 3),
        (3, 4),
        (4, 7),
        (5, 11)
    ]

#test to make sure invalid inputs are raising errors

    for invalid_val in (8.3, 'z', []):
        try:
            fib_out = fibonacci(invalid_val)
            lucas_out = lucas(invalid_val)
            sum_series_out = sum_series(invalid_val)

        except ValueError:
            pass
        else:
            print"Invalid input did not raise error."
            assert False

#series of assertions to test for expected output values for
#each input value per function

    for input_, output in fib_vals:
        assert fibonacci(input_) == output
        assert sum_series(input_) == output

    for input_, output in lucas_vals:
        assert lucas(input_) == output
        assert sum_series(input_) == output
