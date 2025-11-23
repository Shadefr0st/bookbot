import sys

from stats import num_words
from stats import num_char
from stats import sorted_dictionary

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def main():
    
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    word_count = num_words(file_contents)
    char_count = num_char(file_contents)
    sorted_list = sorted_dictionary(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_list:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")



def get_book_text (filepath):
    with open(filepath) as book:
        contents = book.read()
    return contents

main()
