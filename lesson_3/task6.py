def words_title(string_of_words):
    return str.title(' '.join(list(filter(None, string_of_words.split(' ')))))


print(words_title('слово1 '
                  'слово2   слово3'))
