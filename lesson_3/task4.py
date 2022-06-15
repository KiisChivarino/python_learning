def negative_power(base, degree):
    try:
        base = float(base)
        degree = int(degree)
    except ValueError:
        return False
    if degree > -1:
        return False
    result = base
    for i in range(1, degree):
        result = base * base
    return 1 / result


print(negative_power(
    input('Введите основание\n'),
    input('Введите отрицательную степень\n')
))
