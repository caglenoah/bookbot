def count_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    lowered_text = text.lower()
    char_counts = {}
    for char in lowered_text:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file, "r") as f:
        file_contents = f.read()
    total_words = count_words(file_contents)
    print("Total words in the book:", total_words)
    char_counts = char_count(file_contents)
    print("--- Begin report of", path_to_file, "---")
    print(total_words, "words found in document")

    char_list = [{"char": char, "count": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=lambda x: x["count"])

    for char_data in char_list:
        print(f"The '{char_data['char']}' character was found {char_data['count']} times")
    print("--- End report ---")

if __name__ == "__main__":
    main()
