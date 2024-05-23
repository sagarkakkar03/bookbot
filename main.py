def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    len_count = get_word_count(text)
    print(len_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())
main()