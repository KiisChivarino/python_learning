product_list = list()
product_number = int()
characteristic_types = {
    "name": "название",
    "cost": "цена",
    "count": "количество",
    'measure': "ед",
}

while True:
    product_number += 1
    characteristics = {
        characteristic_types['name']: str(),
        characteristic_types['cost']: str(),
        characteristic_types['count']: str(),
        characteristic_types['measure']: str(),
    }
    print('Введите характеристики товара: \n')
    characteristics[characteristic_types['name']] = input('название товара:\n')
    while True:
        cost = input('цена товара (в минорах):\n')
        if not (cost.strip().isdigit()):
            print(f'Значение [{cost}] должно быть целым положительным числом!\n')
            continue
        characteristics[characteristic_types['cost']] = int(cost)
        break
    while True:
        count = input('количество товара:\n')
        if not (count.strip().isdigit()):
            print(f'Значение [{count}] должно быть целым положительным числом!\n')
            continue
        characteristics[characteristic_types['count']] = int(count)
        break
    characteristics[characteristic_types['measure']] = input('единица измерения:\n')
    product = (product_number, characteristics)
    product_list.append(product)
    print('Добавлен товар: ', product)
    ask = input('Ввести следующий товар? (Y,n)\n')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        continue
    else:
        break
analytics = dict()
for product in product_list:
    characteristics = product[1]
    for characteristic_type, characteristic_value in characteristics.items():
        if characteristic_type in analytics:
            analytics[characteristic_type].append(characteristic_value)
        else:
            analytics[characteristic_type] = [characteristic_value]
print(analytics)
