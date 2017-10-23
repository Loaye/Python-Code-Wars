"""
Kata: Duplicate Encoder

#1 Best Practices Solution by Gregism, JS01, wreality, nhpatt, mku, vuiseng9 (plus 15 more warriors)

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])
"""


from collections import Counter

def duplicate_encode(word):
    """encodes a string with '(' and ')'. '(' is equal to solo - ')' is equal to duplicate"""
    word = word.lower()
    new_string = ''
    count = Counter(word)
    for i in word:
        if count[i] == 1:
            new_string += '('
        else:
            new_string += ')'
    return new_string

print(duplicate_encode('recede'))
