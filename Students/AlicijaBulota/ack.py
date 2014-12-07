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

#
#
#test m for inputs 0 to 3, n for inputs 0 to 4

if __name__ == '__main__':
    values = {
        #(m, n): result,
        (0, 0): 1,
        (0, 1): 2,
        (0, 2): 3,
        (0, 3): 4,
        (0, 4): 5,

        (1, 0): 2,
        (1, 1): 3,
        (1, 2): 4,
        (1, 3): 5,
        (1, 4): 6,

        (2, 0): 3,
        (2, 1): 5,
        (2, 2): 7,
        (2, 3): 9,
        (2, 4): 11,

        (3, 0): 5,
        (3, 1): 13,
        (3, 2): 29,
        (3, 3): 61,
        (3, 4): 125
    }

    for input_ in values:
        assert ack(input_[3], input_[2]) == values[input]
#
#
#test implementation of positive integers only

    invalid_input = [
        ('z', 100),
        (*, 37),
        (100, 'a')
    ]

    try:
        output = ack(invalid_input[3], invalid_input[4])
    except ValueError:
        pass
    else:
        raise ValueError(u"No error raised for invalid input")
    print u'All Tests Pass'
