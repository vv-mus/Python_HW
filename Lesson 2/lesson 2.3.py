month = int(input('Введите номер месяца: '))
season = ['зима', 'весна', 'лето', 'осень']
if month == 1 or month == 2 or month == 12:
    print(f'Месяц под номером {month} - {season[0]}')
elif month >= 3 and month <= 5:
    print(f'Месяц под номером {month} - {season[1]}')
elif month >= 6 and month <= 8:
    print(f'Месяц под номером {month} - {season[2]}')
elif month >= 9 and month <= 11:
    print(f'Месяц под номером {month} - {season[3]}')
else:
    print('Вы ввели некорректные данные')
month = int(input('Введите номер месяца: '))
season = {'зима': (1, 2, 12),
          'весна': (3, 4, 5),
          'лето': (6, 7, 8),
          'осень': (9, 10, 11)}
if month >= 1 and month <= 12:
    for key in season.keys():
        if month in season[key]:
            print(f'Месяц под номером {month} - {key}')
else:
    print('Вы ввели некорректные данные')
