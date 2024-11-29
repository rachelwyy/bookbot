from collections import Counter

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_file_contents(path_to_file)
    counter = count_words(file_contents)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{counter} words found in the document")
    print()

    dict_chars = count_chars_dict(file_contents)
    sort = sort_by_values_desc(dict_chars)
    for s in sort:
        if s[0].isalpha():
            print(f"The '{s[0]}' character was found {s[1]} times")

    print("--- End report ---")

def sort_by_values_desc(d):
    return sorted(d.items(), key=lambda item: item[1], reverse=True)

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def count_words(contents):
    return len(contents.split())

def count_chars_dict(contents):
    lowered = contents.lower()
    return dict(Counter(lowered))

main()