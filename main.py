from stats import get_word_count, get_char_counts, get_sorted_char_dict 
import sys

def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    args = sys.argv
    if len(args) == 1 or len(args) > 2:
        print("Usage: python3 main.py <path_to_book>")
        quit(1)

    path =  args[1]
    contents = ""
    try: 
        contents = get_book_text(path)
    except:
        print("No book found matching that path")
        quit(1)
        
    word_count = get_word_count(contents)
    char_count = get_char_counts(contents) 
    sorted_count = get_sorted_char_dict(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_count:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["nums"]}")
    print("============= END ===============")
main()    
