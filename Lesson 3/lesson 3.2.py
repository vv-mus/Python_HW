def info(name, surname, birthday, city, email, phone):
    print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birthday}, Город проживания: {city}, Электронная почта: {email}, Телефон: {phone}')
n = input('Введите имя: ')
s = input('Введите фамилию: ')
b = input('Введите год рождения: ')
c = input('Введите город проживания: ')
e = input('Введите электронный почтовый адрес: ')
p = input('Введите телефон: ')
info(name=n, surname=s, birthday=b, city=c, email=e, phone=p)
