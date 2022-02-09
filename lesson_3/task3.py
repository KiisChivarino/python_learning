def sum_biggest(fistNumber, secondNumber, thirdNumber):
    try:
        number_list = [float(fistNumber), float(secondNumber), float(thirdNumber)]
    except ValueError:
        return False
    number_list.remove(min(number_list))
    return sum(number_list)


print(sum_biggest(1, 2, 3))
