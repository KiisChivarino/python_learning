while True:
    userNumber = input('Введите число\n')
    try:
        firstNumber = int(userNumber)
        break
    except ValueError:
        print(f'Значение [{userNumber}] не является числом!')
        continue

numberString = str(firstNumber)
secondNumber = int(numberString + numberString)
thirdNumber = int(numberString + numberString + numberString)
result = (firstNumber + secondNumber + thirdNumber)
print(result)
