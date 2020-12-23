with open('Data\\5.3.txt', 'r', encoding='UTF-8') as file:
    workers = {}
    av_salary = 0
    amount = 0
    for line in file:
        person, salary = line.split()
        workers[person] = salary
        av_salary += float(salary)
        amount += 1
        if float(salary) < 20000:
            print(f'Сотрудник: {person}, зарплата: {salary}')
    print(f'Средняя величина дохода сотрудников: {(av_salary / amount):.2f}')
