def get_book_text(path_to_file: str) -> str:
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(text: str) -> int:
    word_list = text.split()
    return len(word_list)

def get_char_count(text: str) -> dict:
    char_count = {}

    for c in text:
        act_c = c.lower()
        if act_c in char_count:
            char_count[act_c] += 1
        else:
            char_count[act_c] = 1

    return char_count

def sort_on(items):
    return items["num"]

def sort_counts(counts: dict):
    sorted_list = []
    for c in counts:
        dict_to_append = {}
        dict_to_append["char"] = c
        dict_to_append["num"] = counts[c]
        sorted_list.append(dict_to_append)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
