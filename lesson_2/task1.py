my_first_list = [2, 'text', 456, 45.3, None, 'new_el', True]
my_second_list = [['sublist']]
my_second_list.insert(0, ('cortege', 'into', 'list'))
my_second_list.insert(1, {'set'})
my_second_list.insert(2, {1: 'first_value', 2: 'second_value'})
my_first_list.extend(my_second_list)
list_type_info = dict()
for el in my_first_list:
    list_type_info.update({type(el): el})

print('first list: ')
print(my_first_list)

print('second list: ')
print(my_second_list)

print('type info: ')
print(list_type_info)
