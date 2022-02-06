rating_list = sorted([1, 676, 2, 12, 3, 4, 5, 56, 6, 7, 6], reverse=True)
while True:
    number = input('Введите натуральное число: ')
    if not (number.strip().isdigit() and int(number) > 0):
        print(f'Значение [{number}] должно быть натуральным числом!\n')
        continue
    rating_list.append(int(number))
    rating_list = sorted(rating_list, reverse=True)
    ask = input('Продолжить ввод значений? (Y,n)')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        continue
    else:
        print(rating_list)
        break
