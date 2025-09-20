import sys
from stats import get_book_wordcount
from stats import get_book_charcount
from stats import sort_dictionary

if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

word_count = get_book_wordcount(sys.argv[1])

ch_dic = get_book_charcount(sys.argv[1])

ch_dic_sorted = sort_dictionary(ch_dic)

print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
print(f"Found {word_count} total words\n--------- Character Count -------")
for key in ch_dic_sorted: 
    print(f"{key}: {ch_dic_sorted[key]}")
print("============= END ===============")
