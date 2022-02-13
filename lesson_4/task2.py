def check_el(prev_el, el):
    return prev_el and el > prev_el


base_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = list()
for elem in range(len(base_list)):
    if elem > 0 and base_list[elem - 1] < base_list[elem]:
        result_list.append(base_list[elem])
print(result_list)
