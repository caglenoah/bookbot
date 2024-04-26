def count_words(text):
    words = text.split()
    return len(words)

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    print("Total words in the book:", total_words)

if __name__ == "__main__":
    main()