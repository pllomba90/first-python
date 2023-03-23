def print_upper_words (words):
    for word in words:
        print(word.upper())


def another_print_upper_words(words):
    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())


def another_words_print(words, starts_with):
    for word in words:
        for char in starts_with:
            if word.startswith(char):
                print(word.upper())
                break