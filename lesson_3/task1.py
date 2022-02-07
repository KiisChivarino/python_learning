def is_number(s, non_zero=False):
    try:
        float(s)
        if non_zero and float(s) == float(0):
            return False
        return True
    except ValueError:
        return False


def division(dividend, divider):
    return dividend / divider


while True:
    dividendString = input('Введите делимое:\n')
    if not is_number(dividendString):
        print('Делимое должно быть числом\n')
        continue
    break

while True:
    dividerString = input('Введите делитель:\n')
    if not is_number(dividerString, True):
        print('Делитель должен быть числом, не равным нулю!\n')
        continue
    break

print('Ответ:', dividendString, '/', dividerString, '=', division(float(dividendString), float(dividerString)))
