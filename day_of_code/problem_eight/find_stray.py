"""
Kata - Find the Stray

#1 Best Practice Solutions - cvillian098, snormandeau, Mr.Child, rlqmal, compupro, jsfung83 (plus 8 more warriors)

def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x
"""

def stray(arr):
    """Finds the stray number in a list"""
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    return arr[0]
