from stats import get_book_wordcount
from stats import get_book_charcount
from stats import sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

word_count = get_book_wordcount("/home/toum/workspace/github.com/Toumazou/bookbot/books/frankenstein.txt")

ch_dic = get_book_charcount("/home/toum/workspace/github.com/Toumazou/bookbot/books/frankenstein.txt")

ch_dic_sorted = sort_dictionary(ch_dic)

print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
print(f"Found {word_count} total words\n--------- Character Count -------")
for key in ch_dic_sorted: 
    print(f"{key}: {ch_dic_sorted[key]}")
print("============= END ===============")
