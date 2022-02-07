def print_user_data(**kwargs):
    data_keys = ['имя', 'фамилия', 'дата рождения', 'город проживания', 'email', 'телефон']
    print(dict(zip(data_keys, kwargs.values())))


print_user_data(
    firstName='Иван',
    lastName='Петров',
    birthYear='1980',
    city='Караганда',
    email='mail@mail.ru',
    phone='93563463545'
)
