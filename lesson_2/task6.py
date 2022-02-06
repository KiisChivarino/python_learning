productList = list()
productNumber = int()
characteristicTypes = {
    "name": "название",
    "cost": "цена",
    "count": "количество",
    'measure': "ед",
}

while True:
    productNumber += 1
    characteristics = {
        characteristicTypes['name']: str(),
        characteristicTypes['cost']: str(),
        characteristicTypes['count']: str(),
        characteristicTypes['measure']: str(),
    }
    print('Введите характеристики товара: \n')
    characteristics[characteristicTypes['name']] = input('название товара:\n')
    while True:
        cost = input('цена товара (в минорах):\n')
        if not (cost.strip().isdigit()):
            print(f'Значение [{cost}] должно быть целым положительным числом!\n')
            continue
        characteristics[characteristicTypes['cost']] = int(cost)
        break
    while True:
        count = input('количество товара:\n')
        if not (count.strip().isdigit()):
            print(f'Значение [{count}] должно быть целым положительным числом!\n')
            continue
        characteristics[characteristicTypes['count']] = int(count)
        break
    characteristics[characteristicTypes['measure']] = input('единица измерения:\n')
    product = (productNumber, characteristics)
    productList.append(product)
    print('Добавлен товар: ', product)
    ask = input('Ввести следующий товар? (Y,n)\n')
    if (ask == 'y') | (ask == 'Y') | (ask == ''):
        continue
    else:
        break
analytics = dict()
for product in productList:
    characteristics = product[1]
    for characteristicType, characteristicValue in characteristics.items():
        if characteristicType in analytics:
            analytics[characteristicType].append(characteristicValue)
        else:
            analytics[characteristicType] = [characteristicValue]
print(analytics)
