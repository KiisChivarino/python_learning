my_list = list()
first_value = None
while True:
    first_value = input('Введите значение списка: ')
    ask = input('Продолжить ввод значений? (Y,n)')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        my_list.append(input('Введите значение списка: '))
        my_list.append(first_value)
    else:
        my_list.append(first_value)
        break
    ask = input('Продолжить ввод значений? (Y,n)')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        continue
    else:
        break
print('\n', my_list)
