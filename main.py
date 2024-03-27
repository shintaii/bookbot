def main():
    with open('books/frankenstein.txt') as f:
        file = f.read()

        book_dict = count_letters(file)

        book_dict_list = [{"letter": k, "num": v} for k,v in book_dict.items()]

        book_dict_list.sort(reverse=True, key=sort_on)

        print('--- Begin report of books/frankenstein.txt ---')
        print(f'{number_of_words(file)} words found in the document\n')
        for i in book_dict_list:
            if i["letter"].isalpha():
                print(f'The {i["letter"]} character was found {i["num"]} times')

        print('--- End report ---')


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

def sort_on(dict):
    return dict["num"]




main()