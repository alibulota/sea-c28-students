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
        return sum_series(n - 1, opt_par0, opt_par1) +
        sum_series(n - 2, opt_par0, opt_par1)

if __name__ == '__main__':
    fib_vals = []
