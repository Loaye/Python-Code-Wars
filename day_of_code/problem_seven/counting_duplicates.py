"""
Kata - Counting Duplicates

#1 Best Practice Solutions by tpatja, nkrause323, alpen0, lixiang

def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])\
"""


def duplicate_count(text):
    """counts duplicated letters in a give word"""
    new_text = text.lower()
    repeated = []
    for letter in new_text:
        if letter not in repeated and new_text.count(letter) > 1:
            repeated.append(letter)
    return len(repeated)
