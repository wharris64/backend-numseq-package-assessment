"""[returns fib number of the nth sequence]

exports fib(n)
"""
def fib(n):
    """[returns fib number of the nth sequence]
    
    Arguments:
        n {[int]} -- [integer to be manipulated]
    
    Returns:
        [int] -- [integer after manipulation]
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
