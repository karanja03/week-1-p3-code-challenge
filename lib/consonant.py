def consonant_find(word):
    consonant_values = {'b': 2, 'c': 3, 'd': 4, 'f': 6, 'g': 7, 'h': 8, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 
                        'n': 14, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'v': 22, 'w': 23, 'x': 24, 
                        'y': 25, 'z': 26}

    consonants = 'bcdfghjklmnpqrstvwxyz'
    max_value = 0
    current_value = 0

    for char in word.lower():
        if char in consonants:
            current_value += consonant_values[char]
        else:
            max_value = max(max_value, current_value)
            current_value = 0

    return max(max_value, current_value)

