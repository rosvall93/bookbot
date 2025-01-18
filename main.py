def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    list = word_list(text)
    sorted_list = the_sorter(list)
    sorted_list.sort(reverse=True, key=sort)
    print(f"{num_words} words found in the document", sorted_list)

def sort(sorted_list):
    return sorted_list["num"]


def the_sorter(dict):
    a = []
    for key in dict:
        count = dict[key]
        if key.isalpha() == True:
            new_dict = {"char": key, "num": count}
            a.append(new_dict)
    return a

        
def word_list(letters):
    freq = {}
    for f in letters:
        lower_letters = f.lower()
        if lower_letters in freq:
            freq[lower_letters] += 1
        else:
            freq[lower_letters] = 1
    return freq
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

