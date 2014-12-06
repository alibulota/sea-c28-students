def ack(m, n):
    """Ackermann function with input validation,
    return None for invalid input"""
    if (not isinstance(m, int)) or (not isinstance(n, int)):
        raise ValueError
    if (m < 0) or (n < 0):
        return None
    if m == 0:
        return (n + 1)
    elif n == 0:
        return ack(m - 1, 1)
    else:
        m > 0
        return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':
    values = {}
