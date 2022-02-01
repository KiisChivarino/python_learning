while True:
    income = input('Введите доход фирмы (в минорных единицах)\n')
    if not (income.strip().isdigit()):
        print(f'Значение [{income}] должно быть целым положительным числом!')
        continue
    break
while True:
    costs = input('Введите издержки фирмы (в минорных единицах)\n')
    if not (income.strip().isdigit()):
        print(f'Значение [{costs}] должно быть целым положительным числом!')
        continue
    break
income = int(income)
costs = int(costs)
if income > costs:
    print('Выручка больше издержек!')
elif costs > income:
    print('Издержки больше выручки!')
else:
    print('Издержки равны выручке')
