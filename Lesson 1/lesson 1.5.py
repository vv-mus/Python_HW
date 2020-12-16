proc = float(input('Введите выручку организации: '))
cos = float(input('Введите издержки организации: '))
if proc > cos:
    prof = proc / cos
    print(f'Организация работает с прибылью. Рентабильность равна {prof:.2f}.')
    workers = int(input('Сколько человек работает в организации? '))
    prof_worker = prof / workers
    print(f'Прибыль на одного сотрудника составила {prof_worker:.2f}.')
elif proc == cos:
    print('Выручка и издержки равны.')
else:
    print('Организация работает в убыток.')