def num_words (book):
    words = len(book.split())
    return words

def num_char (book):
    char_count = {}
    for char in book:
        lower_char = char.lower()
        if lower_char in char_count:
            char_count[lower_char] += 1
        else:
            char_count[lower_char] = 1

    return char_count

def sort_on(items):
    return items["num"]

def sorted_dictionary (chars):
    char_count = []
    for pair in chars:
        char_dict = {"char": pair, "num": chars[pair]}
        char_count.append(char_dict)

    char_count.sort(reverse=True, key=sort_on)
    return char_count
