while True:
    userString = input('Введите число\n')
    if not (userString.isdigit()):
        print(f'Значение [{userString}] не является целым положительным числом!')
        continue
    break

maxNumber = 0
i = 0
while i < len(userString):
    currentNumber = int(userString[i])
    if currentNumber > maxNumber:
        maxNumber = currentNumber
    if maxNumber == 9:
        break
    i += 1
print(maxNumber)
