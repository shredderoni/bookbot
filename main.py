import sys
from stats import count_words, num_of_char, sorted_dictionary

def get_book_text(path):
    with open(path) as f:
        content = f.read()
    return content

def main():
    print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = count_words(text)
    char_dict = num_of_char(text)
    char_count_new = sorted_dictionary(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count_new:
        if item["name"].isalpha() == True:
            print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")

main()
