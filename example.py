class BadDenominatorError(ZeroDivisionError):
    pass

def div(x, y):
    """
    Returns the quotient of dividing x by y.
    Will raise BadDenominatorError if y is 0.
    """
    if y == 0:
        raise BadDenominatorError()
    return x / y

def add(x, y):
    t = 0
    while t <y:
        x += 1
        t += 1
    return x

