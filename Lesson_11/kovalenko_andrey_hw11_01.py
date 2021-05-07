'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class ExDate:
    def __init__(self, dts):
        # Проверяем дату на корректность.
        if self.validate(dts):
            # Метод класса - запомнит дату.
            ExDate.process_date(dts)
        else:
            # В противном случае - ничего не делаем, и ругаемся.
            raise Exception('Некорректная дата!')

    @classmethod
    def process_date(cls, dts):
        # Ракладываем дату и запоминаем в hInstance класса.
        # Сюда мы попадаем только в том случае, когда прошли проверку корректности.
        cls.d_day = int(dts.split('-')[0])
        cls.d_month = int(dts.split('-')[1])
        cls.d_year = int(dts.split('-')[2])

    @staticmethod
    def validate(dts=''):
        # Валидатор даты.
        validity = {'d': 1, 'm': 1, 'y': 1}

        d_year = 0
        d_month = 0

        s_day = dts.split('-')[0]
        s_month = dts.split('-')[1]
        s_year = dts.split('-')[2]

        # Проверим месяц.
        try:
            d_month = int(s_month)
            if d_month > 12 or d_month < 1:
                validity['m'] = 0
        except:
            validity['m'] = 0

        # Првоерим год
        try:
            d_year = int(s_year)
            if d_year > 4000 or d_year < 1900:
                validity['y'] = 0
        except:
            validity['y'] = 0

        # Если год и месяц прошли проверку - то проверяем какой день.
        if validity.get('y', 0) == 1 and validity.get('m', 0) == 1:
            try:
                d_day = int(s_day)
                if d_year % 4 == 0 and d_month == 2:
                    if d_day > 29 or d_day < 1:
                        validity['d'] = 0
                elif d_month == 2:
                    if d_day > 28 or d_day < 1:
                        validity['d'] = 0
                elif d_month in (1, 3, 5, 7, 8, 10, 12) and (d_day > 31 or d_day < 1):
                    validity['d'] = 0
                elif d_day > 30 or d_day < 1:
                    validity['d'] = 0
            except:
                validity['d'] = 0

        # Сумма всех успешных проверок = 3.
        if sum(validity.values()) == 3:
            return True
        else:
            return False

    # Отобразим дату в нормальном человеческом виде.
    def __str__(self):
        return "{:02d}/{:02d}/{:04d}".format(self.d_day, self.d_month, self.d_year)


my_date = ExDate('1-2-2021')
print(my_date)
