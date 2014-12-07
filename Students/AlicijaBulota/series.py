#Fibonacci Series


def fibonacci(n):
    """Fibonacci series function to return
    nth value in series using recursion"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#Lucas Numbers


def lucas(n):
    """function to find nth value for
    Lucas Numbers"""
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)
