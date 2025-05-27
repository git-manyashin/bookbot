import sys
from stats import count_words, get_book_text, count_letters, get_sorted_letter_counts

def main():
    # ✅ Check for command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    
    # Count words and letters
    word_count = count_words(book_text)
    letter_count = count_letters(book_text)
    sorted_letters = get_sorted_letter_counts(letter_count)

    # Print formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for entry in sorted_letters:
        print(f"{entry['char']}: {entry['num']}")
    
    print("============= END ===============")

main()