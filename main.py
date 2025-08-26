import stats
import sys

path = f'/home/sala/boot_dev_projects/github.com/bookbot/'

def get_book_text(path, book):
    with open((path + book)) as f:
        return f.read()
    
def main():
    print(get_book_text(path))              

if __name__ == "__main__":
    if not sys.argv[1]: print('Usage: python3 main.py <path_to_book>')
    else:
        book = get_book_text(path, f'{sys.argv[1]}')
        print(stats.get_num_words(book))
        count = stats.count_characters(book)
        #print(count)
        dic_count = stats.transformed_dictonary(count)
        #print(dic_count)
        sorted_count = stats.sorted_count(dic_count)
        for i in sorted_count:
            print(f'{i[0]}: {i[1]}')
    