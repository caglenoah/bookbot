def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] +=1
            else: char_counts[char] = 1
    print(char_counts)


    

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    print("Total words in the book:", total_words)
    char_count(file_contents)

if __name__ == "__main__":
    main()