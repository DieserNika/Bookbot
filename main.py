import sys

from stats import count_chars, count_words, sort_list


# reads file and returns to read text as f'string
def get_book_txt(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def main():
    # defines a given filepath
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        filepath = sys.argv[1]
    else:
        print("ERR: too many arguments | Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # sets variable to read text as f'string
    book_txt = get_book_txt(filepath)

    # calling count_words() and count_chars()
    word_count = count_words(book_txt)
    char_count = count_chars(book_txt)

    # sorting
    sorted_list = sort_list(char_count)

    # formatting console log and printing
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for i in sorted_list:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")

    print("============= END ===============")


main()
