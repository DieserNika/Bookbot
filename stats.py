# DESC: iterates and splits a string by spaces and therefore counts the words
def count_words(file):
    num = 0
    for i in file.split(None, -1):
        num += 1

    return num


# DESC: converts a file to lowercase, creating a dict, adds chars if not in num, else increments value by 1
def count_chars(file):
    conv_txt = file.lower()
    num = {}

    for char in conv_txt:
        if char in num:
            num[char] += 1
        else:
            num[char] = 1

    return num


# DESC: difines key for sort_list()
def sort_by(item):
    return item["num"]


# DESC: creates list, iterates over it, creates and appends dict in list, sorts with sort_by() and returns list
def sort_list(chars):
    list = []

    for c, n in chars.items():
        list.append(dict(char=c, num=n))

    list.sort(reverse=True, key=sort_by)

    return list
