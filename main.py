def get_book_text(file_path):
    file_contents = ""
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(book):
    return len(book.split())

def main():
    contents = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(contents)
    print(f"Found {word_count} total words")

main()    
