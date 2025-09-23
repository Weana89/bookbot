import sys

from stats import get_book_text, get_word_count, get_char_count, sort_counts

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path_to_book = sys.argv[1]

    book_content = get_book_text(path_to_book)
    number_of_words = get_word_count(book_content)
    number_of_chars = get_char_count(book_content)
    sorted_chars = sort_counts(number_of_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for sc in sorted_chars:
        print(f'{sc["char"]}: {sc["num"]}')
    print("============= END ===============")

main()