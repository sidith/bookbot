book_path = "books/frankenstein.txt"
char_counts = {
        "a" : 0,
        "b" : 0
}

def main():
    word_count = 0
    content = ""

    with open(book_path) as file:
       content = file.read()
    
    print(f"--- Begin report of {book_path} ---")
    count_words(content)
    print()
    count_chars(content)
    print("--- End Report ---")

def count_words(content):
    words = content.split()
    print(f"{len(words)} words found in the document")

def sort_on(dict):
    return dict["count"]

def count_chars(content):
    raw_chars = [c for c in content.strip().lower() if c.isalpha()]
    for char in raw_chars:
        if not char in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    char_counts_list = []
    for char in char_counts:
        char_counts_list.append({"char": char, "count": char_counts[char]})
    char_counts_list.sort(reverse=True, key=sort_on)
    for char_count in char_counts_list:
        print(f"The '{char_count['char']}' character was found {char_count['count']} times")

main()
