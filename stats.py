def get_book_wordcount(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return len(file_contents.split())

def get_book_charcount(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    file_contents_lower = file_contents.lower()
    dictionary = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0,
            "æ": 0,
            "â": 0,
            "ê": 0,
            "ë": 0,
            "ô": 0
    }
    for char in file_contents_lower:
        if char in dictionary:
            dictionary[char] = dictionary[char] + 1
    return dictionary

dictionary = get_book_charcount("/home/toum/workspace/github.com/Toumazou/bookbot/books/frankenstein.txt")

for key in dictionary:
    print(f"{key}: {dictionary[key]}")

