while True:
    income = input('Введите доход фирмы (в минорных единицах)\n')
    if not (income.strip().isdigit()):
        print(f'Значение [{income}] должно быть целым положительным числом!\n')
        continue
    break
while True:
    costs = input('Введите издержки фирмы (в минорных единицах)\n')
    if not (income.strip().isdigit()):
        print(f'Значение [{costs}] должно быть целым положительным числом!\n')
        continue
    break
income = int(income)
profit = income - int(costs)

profitability = profit / income

print(f'Рентабельность фирмы равна: {profit / income}')

while True:
    personalCount = input('Введите количество сотрудников\n')
    if not (personalCount.strip().isdigit() and int(income) > 0):
        print(f'Значение [{income}] должно быть натуральным числом!\n')
        continue
    break

if profit > 0:
    personProfit = profit / int(personalCount)
else:
    personProfit = 0

print(f'Прибыль на одного сотрудника равна: {personProfit}')
