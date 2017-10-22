"""
Kata - Shortest Word

#1 Best Solution Practices by MiraliN, Cptnprice, FranzSchubert92, Chris_Rands, Mr.Child, gallione11 (plus 41 more warriors)

def find_short(s):
    return min(len(x) for x in s.split())
"""

def find_short(words):
    """finds the shortest word in a string and returns it"""
    list_words = list(words.split(" "))
    shortest_word = list_words[0]
    for word in list_words:
        if len(word) < len(shortest_word):
            shortest_word = word
    return len(shortest_word)
