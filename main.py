def get_word_count(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def main():
    with open("books/frankenstein.txt") as f:
        content = f.read()
    
    word_count = get_word_count(content)
    char_counts = count_characters(content)

    letter_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            letter_list.append({"char": char, "count": count})

    def sort_on(dict):
        return dict["count"]
    
    letter_list.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    
    for item in letter_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

    print("--- End report ---")

if __name__ == "__main__":
    main()