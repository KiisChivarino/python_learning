import re


def sum_a_string_of_numbers(string_of_numbers, separator=' '):
    return sum(list(map(int, list(filter(None, string_of_numbers.split(separator))))))


sum_of_numbers = int()
print('Добавляйте числа через пробел; для завершения добавьте точку')
while True:
    string_of_numbers = input()
    if re.search('[^\d .]', string_of_numbers):
        print('Необходимо вводить только числа через пробел или точку!')
        continue
    if '.' in string_of_numbers:
        sum_of_numbers += sum_a_string_of_numbers(string_of_numbers.split('.')[0])
        break
    sum_of_numbers += sum_a_string_of_numbers(string_of_numbers)
print(sum_of_numbers)
