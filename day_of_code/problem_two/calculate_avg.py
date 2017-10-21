"""
Kata : Calculate Average

#1 Best Practices Solution by mirat, Malavolent, tedmiston, riyakayal, tachyonlabs, Parabellum117 (plus 108 more warriors)

def find_average(array):
    return sum(array) / len(array) if array else 0

"""

def find_average(array):
    """Calculates the average of a given array"""
    if len(array) == 0:
        return 0
    return sum(array) / len(array)
