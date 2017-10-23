"""getting a series of a sum of nth"""

def series_sum(n):
    """gets sum series of a group numbers"""
    if n == 0:
        return '0.00'
    sum = 1.00
    d = 4
    for i in range(1, n):
        sum = sum + (1 / d)
        d = d + 3
    return '%.2f' % sum
