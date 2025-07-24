def count_words(text):
    split_text = text.split() 
    num_words = 0
    for word in split_text:
        num_words += 1
    return num_words

def num_of_char(text):
    char_dict = {}
    for letter in text.lower():
        if letter in char_dict:
            char_dict[letter] += 1
        else:
            char_dict[letter] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dictionary(dict):
    list_of_dict = []
    for item in dict:
        new_dict = {}
        new_dict["name"] = item
        new_dict["num"] = dict[item]
        list_of_dict.append(new_dict)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

