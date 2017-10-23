"""
Kata - Replace With Alphabet Position

#1 Best Solutions Practices by laoris, murpium, CrazyMerlyn, datagram, Karan@CodeDoor, thamiamrani (plus 13 more warriors)

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
"""


def alphabet_position(text):
    """Converts a string into a new one with letters corresponding to index value"""
    small = text.lower()
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    converted = ""
    for chr in small:
        if chr in alphabet:
            converted += str(alphabet.index(chr) + 1) + " "
    return converted[:-1]
