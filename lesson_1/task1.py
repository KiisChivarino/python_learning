intVar = int()
stringVar = str()
floatVar = float()
userValue = str()

print(format(f'integer value: [{intVar}]\nstring value: [{stringVar}]\nfloat value: [{floatVar}]'))

while True:
    userValue = input('Введите целое число\n')
    try:
        intVar = int(userValue)
        break
    except ValueError:
        print(f'Значение [{userValue}] не является целым числом!')
        continue

stringVar = input('Введите строку\n')

while True:
    userValue = input('Введите десятичную дробь\n')
    try:
        floatVar = float(userValue)
        break
    except ValueError:
        print(f'Значение [{userValue}] не является десятичной дробью!')
        continue
print(str('Целое число: [{:d}]\nСтрока: [{}]\nДесятичная дробь: [{:f}]').format(intVar, stringVar, floatVar))
