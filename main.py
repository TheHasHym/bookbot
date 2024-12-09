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


def print_report(text):
    chars = count_chars(text)
    chars = sorted(chars.items(), key=lambda char: char[1], reverse=True)

    words = count_words(text)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words fount in the document")
    print("")
    for char in chars:
        if char[0].isalpha():
            print(f"The '{char[0]}' character was found '{char[1]}' times")
    print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")


main()
