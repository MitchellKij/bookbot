from stats import get_number_of_words, get_character_freq, get_sorted_character_freq
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

pathToBook = sys.argv[1]

def get_book_text(pathToBook):
    with open(pathToBook, 'r', encoding='utf-8') as file:
        book_text = file.read()
    return book_text

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {pathToBook}...")
    book_text = get_book_text(pathToBook)
    print("----------- Word Count ----------")
    word_count = get_number_of_words(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_freq = get_character_freq(book_text)
    sorted_char_freq = get_sorted_character_freq(char_freq)
    for entry in sorted_char_freq:
        char = entry['char']
        num = entry['num']
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()