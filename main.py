def main():
    with open('books/frankenstein.txt') as f:
        file = f.read()

        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{number_of_words(file)} words found in the document')
        print(count_letters(file))


def number_of_words(file):
    words = file.split()

    return len(words)

def count_letters(file):
    letter_hash = {}
    for letter in file:
        if letter.lower() in letter_hash:
            letter_hash[letter.lower()] += 1
        else:
            letter_hash[letter.lower()] = 1

    return letter_hash
        


main()