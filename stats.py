def get_word_count(book):
    return len(book.split())

def get_char_counts(book_text):
    char_dict = {}
    for char in book_text:
        lower = char.lower()
        if char_dict.get(lower):
            char_dict[lower] = char_dict.get(lower) + 1
        else:
            char_dict[lower] = 1
    return char_dict


def get_sorted_char_dict(char_dict):
    new_dict = []
    for char in char_dict:
        new_dict.append({"char": char, "nums": char_dict[char]})

    def sort_on(items):
        return items["nums"]

    new_dict.sort(reverse=True, key=sort_on)
    
    return new_dict
    

