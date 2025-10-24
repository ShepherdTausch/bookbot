def get_word_count(txt):
    words = txt.split()
    return len(words)

def num_key_value(data):
    return data["num"]

def sort_dict(d):
    new_list = []
    for key in d:
        if key.isalpha():
            new_list.append({"char": key, "num": d[key]})
    new_list.sort(reverse=True, key=num_key_value)
    return new_list


def get_char_count(txt):
    letters = list(txt)
    chars_dict = {}
    for char in letters:
        letter = char.lower()
        if letter in chars_dict:
            chars_dict[letter] += 1
        else:
            chars_dict[letter] = 1
    return chars_dict

# print(sort_dict({"t": 29493, "h": 19176, "e": 44538, "p": 5952, "r": 20079}))
