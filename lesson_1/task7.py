IMPROVEMENT_PERCENT = 0.1
dayNumber = 1

while True:
    firstResultKm = input('Введите в километрах результат спортсмена в первый день\n')
    if not (firstResultKm.strip().isdigit()):
        print(f'Значение [{firstResultKm}] должно быть целым положительным числом!')
        continue
    firstResultKm = int(firstResultKm)
    break
while True:
    finalResultKm = input('Введите в километрах желаемый результат спортсмена\n')
    if not (finalResultKm.strip().isdigit()):
        print(f'Значение [{finalResultKm}] должно быть целым положительным числом!')
        continue
    finalResultKm = int(finalResultKm)
    break
currentResultKm = firstResultKm
while currentResultKm <= finalResultKm:
    dayNumber += 1
    currentResultKm += currentResultKm * IMPROVEMENT_PERCENT

print(f'На {dayNumber}-й день спортсмен достиг результата — не менее {finalResultKm} км')
