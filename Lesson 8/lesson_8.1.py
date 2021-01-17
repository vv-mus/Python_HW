class Date:
    def __init__(self, date):
        self.date = Date.transform(date)

    @classmethod
    def transform(cls, date):
        day, month, year = date.split('-')
        return Date.validate(int(day), int(month), int(year))

    @staticmethod
    def validate(day, month, year):
        m_d31 = [1, 3, 5, 7, 8, 10, 12]
        m_d30 = [4, 6, 9, 11]
        if 1900 <= year <= 2050:
            if month in m_d31:
                if 1 <= day <= 31:
                    print('Все корректно.')
                else:
                    print('Неправильно введен день!')
            elif month in m_d30:
                if 1 <= day <= 30:
                    print('Все корректно.')
                else:
                    print('Неправильно введен день!')
            elif month == 2:
                if 1 <= day <= 28:
                    print('Все корректно.')
                else:
                    print('Неправильно введен день!')
            else:
                print('Неправильно введен месяц!')
        else:
            print('Неправильно введен год!')


try:
    date = Date(input('Введите дату в формате dd-mm-yyyy: '))
except ValueError:
    print('Неправильный формат даты!')
