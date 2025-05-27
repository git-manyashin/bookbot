# stats.py
# This function reads the contents of a file and returns it as a string.
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

# This function counts the number of words in a given text.
def count_words(file_contents):
    words = file_contents.split()
    return len(words)

# This function counts the number of letters in a given text.
def count_letters(file_contents):
    char_counts = {}
    for char in file_contents:
        lower_char = char.lower()
        if lower_char in char_counts:
            char_counts[lower_char] += 1
        else:
            char_counts[lower_char] = 1
    return char_counts


# Sort dictionary
def sort_on(d):
    return d["num"]

def get_sorted_letter_counts(char_dict):
    sorted_list = []

    for char, count in char_dict.items():
        if char.isalpha():  # only include letters
            sorted_list.append({"char": char, "num": count})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list