list_from_string = list(filter(None, input('Введите строку\n').split(' ')))
for word in list_from_string:
    print(int(list_from_string.index(word)) + 1, word[:10])
