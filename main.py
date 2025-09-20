from stats import get_book_wordcount
from stats import get_book_charcount

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

word_count = get_book_wordcount("/home/toum/workspace/github.com/Toumazou/bookbot/books/frankenstein.txt")

print(f"{word_count} words found in the document")

char_dictionary = get_book_charcount("/home/toum/workspace/github.com/Toumazou/bookbot/books/frankenstein.txt")

for key in char_dictionary: 
    print(f"'{key}': {char_dictionary[key]}")
