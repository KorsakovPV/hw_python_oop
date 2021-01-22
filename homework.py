import datetime as dt


class Record:
    """
    Класс используется только для хранения данных записей.
    """

    def __init__(self, amount, comment, date=None):
        date_format = '%d.%m.%Y'

        if date is None:
            date = dt.datetime.now()

        else:
            date = dt.datetime.strptime(date, date_format)

        self.amount = amount
        self.comment = comment
        self.date = date.date()


class Calculator:
    """
    Базовый класс. Реализует общие методы.
    """

    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        today = dt.datetime.now().date()
        spend_today = sum([i.amount if i.date == today else 0
                           for i in self.records])
        return spend_today

    def get_week_stats(self):
        end_week = dt.datetime.now().date()
        start_week = end_week - dt.timedelta(days=6)
        spend_week = sum(
            [i.amount if end_week >= i.date >= start_week else 0 for i in
             self.records]
        )
        return spend_week


class CashCalculator(Calculator):
    """
    Класс наследует базовый класс и реализует весь функционал связанный с
    деньгами.
    """

    USD_RATE = 60.00
    EURO_RATE = 70.00

    def get_today_cash_remained(self, currency):
        spend_today = self.get_today_stats()
        answer = {'rub': [1, 'руб'],
                  'usd': [self.USD_RATE, 'USD'],
                  'eur': [self.EURO_RATE, 'Euro']}
        remains = abs(self.limit - spend_today)
        exchange_rate, currency_type = answer[currency]

        if spend_today == self.limit:
            return 'Денег нет, держись'

        elif spend_today < self.limit:
            answer_str = 'На сегодня осталось'

        elif spend_today > self.limit:
            answer_str = 'Денег нет, держись: твой долг -'

        return '{0} {1} {2}'.format(answer_str, round(remains / exchange_rate,
                                                      2), currency_type)


class CaloriesCalculator(Calculator):
    """
    Класс наследует базовый класс и реализует весь функционал связанный с
    калориями.
    """

    def get_calories_remained(self):
        get_calories_today = self.get_today_stats()

        if get_calories_today < self.limit:
            remains = self.limit - get_calories_today

            return 'Сегодня можно съесть что-нибудь ещё, но с общей ' \
                   'калорийностью не более {} кКал'.format(remains)
        return 'Хватит есть!'


# data for testing
if __name__ == '__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(
        Record(amount=150, comment='Test 37', date='01.9.2019'))
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(
        Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
    cash_calculator.add_record(
        Record(amount=145, comment='Безудержный шопинг', date='08.03.2019'))
    cash_calculator.add_record(
        Record(amount=1568, comment='Наполнение потребительской корзины',
               date='09.03.2019'))
    cash_calculator.add_record(
        Record(amount=691, comment='Катание на такси', date='08.03.2019'))
    assert cash_calculator.get_today_cash_remained(
        'rub') == 'На сегодня осталось 555.0 руб'
    assert cash_calculator.get_today_cash_remained(
        'usd') == 'На сегодня осталось 9.25 USD'
    assert cash_calculator.get_today_cash_remained(
        'eur') == 'На сегодня осталось 7.93 Euro'
    assert cash_calculator.get_today_stats() == 445
    cash_calculator.add_record(Record(amount=555, comment='Продукты'))
    assert cash_calculator.get_today_cash_remained(
        'rub') == 'Денег нет, держись'
    assert cash_calculator.get_today_stats() == 1000
    cash_calculator.add_record(Record(amount=7500, comment='Монитор'))
    assert cash_calculator.get_today_cash_remained(
        'rub') == 'Денег нет, держись: твой долг - 7500.0 руб'
    assert cash_calculator.get_today_cash_remained(
        'usd') == 'Денег нет, держись: твой долг - 125.0 USD'
    assert cash_calculator.get_today_cash_remained(
        'eur') == 'Денег нет, держись: твой долг - 107.14 Euro'
    assert cash_calculator.get_today_stats() == 8500
    assert cash_calculator.get_week_stats() == 8500
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='05.04.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='04.04.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='03.04.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='02.04.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='01.04.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='31.03.2020'))
    cash_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='30.03.2020'))
    cash_calculator.add_record(
        Record(amount=1000000, comment='Продукты', date='29.03.2020'))
    cash_calculator.add_record(
        Record(amount=1000000, comment='Продукты', date='28.03.2020'))
    assert cash_calculator.get_week_stats() == 8500

    calories_calculator = CaloriesCalculator(2000)
    calories_calculator.add_record(Record(amount=145, comment='кофе'))
    assert calories_calculator.get_calories_remained() == 'Сегодня можно съе' \
                                                          'сть что-нибудь ещ' \
                                                          'ё, но с общей кал' \
                                                          'орийностью не бол' \
                                                          'ее 1855 кКал'
    calories_calculator.add_record(Record(amount=500, comment='творог'))
    calories_calculator.add_record(Record(amount=500, comment='йогурт'))
    assert calories_calculator.get_calories_remained() == 'Сегодня можно съе' \
                                                          'сть что-нибудь ещ' \
                                                          'ё, но с общей кал' \
                                                          'орийностью не бол' \
                                                          'ее 855 кКал'
    calories_calculator.add_record(Record(amount=855, comment='торт'))
    assert calories_calculator.get_calories_remained() == 'Хватит есть!'
    calories_calculator.add_record(Record(amount=855, comment='торт'))
    assert calories_calculator.get_calories_remained() == 'Хватит есть!'
    assert calories_calculator.get_week_stats() == 2855
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='05.04.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='04.04.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='03.04.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='02.04.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='01.04.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='31.03.2020'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Продукты', date='30.03.2020'))
    calories_calculator.add_record(
        Record(amount=1000000, comment='Продукты', date='29.03.2020'))
    calories_calculator.add_record(
        Record(amount=1000000, comment='Продукты', date='28.03.2020'))
    assert calories_calculator.get_week_stats() == 2855
