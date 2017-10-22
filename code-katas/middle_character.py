"""
Kata: Get the Middle Character

#1 Best Practices Solution : hiasen, kit9ra, GNX, niedyszyn, RandomJack, pstryq (plus 39 more warriors)

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]

"""


def get_middle(s):
    """Gets the middle letter of a string - even returns 2 middles"""
    if len(s) % 2 == 0:
        return s[int(len(s) / 2) - 1] + s[int(len(s) / 2)]
    else:
        return s[int(len(s) / 2)]
