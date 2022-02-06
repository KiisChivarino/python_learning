user_value = str()
user_month = int()
seasons = {'зима': [12, 1, 2], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

while True:
    user_value = input('Введите номер месяца\n')
    if not (user_value.strip().isdigit() and (1 > int(user_value) or int(user_value) > 12)):
        print(f'Значение [{user_value}] должно быть целым положительным числом от 1 до 12!\n')
        continue
    user_month = int(user_value)
    break

for season, month in seasons.items():
    if user_month in month:
        print(f'Время года - {season}')
        break
