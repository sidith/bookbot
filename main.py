book_path = "books/frankenstein.txt"


def main():
    word_count = 0
    content = ""

    with open(book_path) as file:
       content = file.read()

    words = content.split()

    count_words(words)

def count_words(words):
    print(len(words))

main()
