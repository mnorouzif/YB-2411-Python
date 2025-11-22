import doctest
def add(a, b):
    """
    Returns the sum of two numbers.

    Example:
    >>> add(2, 4)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    
    doctest.testmod()
