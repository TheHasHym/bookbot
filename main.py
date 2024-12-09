def count_words(text):
    with open(text) as f:
        file = f.read()
        split_txt = file.split()
        words = 0
        for word in split_txt:
            words += 1
        return words

def count_chars(text):
    with open(text) as f:
        file = f.read().lower()
        chars = {}
        for char in file:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        return chars


def main():
    print(count_words("books/frankenstein.txt"))
    print(count_chars("books/frankenstein.txt"))

main()
