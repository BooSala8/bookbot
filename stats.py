import string

def get_chars(book):
    return book.split()

def get_num_words(book):
    return f'Found {len(get_chars(book))} total words'

def count_characters(book):
    lower = book.lower()
    words = get_chars(lower)
    count = {}
    for word in words:
        for letter in word:
            if letter in count: count[letter] += 1
            else: count[letter] = 1
    return count

def transformed_dictonary(letter_count:dict):
    transformed = []
    for letter, count in letter_count.items():
        if letter.isalpha():
            current_dic = {'char': letter, 'num': count}
            transformed.append(current_dic)
    return transformed

def sort_on(item:list):
    return item['num']

def sorted_count(sorted_list: list):
    filtered = sorted(sorted_list, key=sort_on, reverse=True)
    individual_values = [(i['char'], i['num']) for i in filtered]
    return individual_values


