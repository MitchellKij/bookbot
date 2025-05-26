def get_number_of_words(text):
    words = text.split()
    return len(words)


def get_character_freq(text):
    frequencies = {}
    for char in text.lower():
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

def get_sorted_character_freq(frequencies):
    sorted_frequencies = [{"char": char, "num": count} for char, count in frequencies.items()]
    sorted_frequencies.sort(key=lambda x: x["num"], reverse=True)
    return sorted_frequencies