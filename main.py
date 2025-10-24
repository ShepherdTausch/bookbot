from stats import *
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_char(list):
    for dict in list:
        print(f"{dict["char"]}: {dict["num"]}")

def main():
    book_location = sys.argv[1]
    book_text = get_book_text(book_location)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    char_count = get_char_count(book_text)
    list = sort_dict(char_count)
    print_char(list)
    print("============= END ===============")

main()
