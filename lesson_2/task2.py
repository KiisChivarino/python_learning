myList = list()
firstValue = None
while True:
    firstValue = input('Введите значение списка: ')
    ask = input('Продолжить ввод значений? (Y,n)')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        myList.append(input('Введите значение списка: '))
        myList.append(firstValue)
    else:
        myList.append(firstValue)
        break
    ask = input('Продолжить ввод значений? (Y,n)')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        continue
    else:
        break
print('\n', myList)
