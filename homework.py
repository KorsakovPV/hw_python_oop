import datetime as dt

class Record: #Complite
    def __init__(self, amount, comment, date=None):
        date_format = '%d.%m.%Y'
        if date==None: date = dt.datetime.now()
        else: date=dt.datetime.strptime(date, date_format)
        self.amount=amount
        self.comment=comment
        self.date=date.date()

class Calculator: #complite
    def __init__(self, limit):
        self.limit=limit
        self.records=[]


    def add_record(self, record): #complite
        self.records.append(record)

    def get_today_stats(self): #complite
        spend_today=0
        today=dt.datetime.now().date()
        
        for i in self.records:
#            print(i.date,today)
            if i.date==today:
                spend_today+=i.amount
        return spend_today

    def get_week_stats(self): #complite
        spend_week=0
        end_week=dt.datetime.now().date()
        start_week=end_week - dt.timedelta(days=6)
        for i in self.records:
            if i.date<=end_week and i.date>=start_week:
                spend_week+=i.amount
        return spend_week            

class CashCalculator(Calculator): #complite
    USD_RATE = 60.00
    EURO_RATE = 70.00
    def get_today_cash_remained(self, currency):
#        self.USD_RATE = 60.00
#        self.EURO_RATE = 70.00
        spend_today=(self.get_today_stats())
        if spend_today==self.limit:
            return('Денег нет, держись')
        elif spend_today<self.limit:
            answer='На сегодня осталось'
            if currency=='rub':
                remains=(self.limit-spend_today)
                return(answer+' {:.1f} руб'.format(remains))
            elif currency=='usd':
                remains=(self.limit-spend_today)/self.USD_RATE
                return(answer+' {:.1f} USD'.format(remains))
            elif currency=='eur':
                remains=(self.limit-spend_today)/self.EURO_RATE
                return(answer+' {:.2f} Euro'.format(remains))
        elif spend_today>self.limit:
            answer='Денег нет, держись: твой долг -'
            if currency=='rub':
                remains=abs(self.limit-spend_today)
                return(answer+' {:.1f} руб'.format(remains))
            elif currency=='usd':
                remains=abs((self.limit-spend_today)/self.USD_RATE)
                return(answer+' {:.1f} USD'.format(remains))
            elif currency=='eur':
                remains=abs((self.limit-spend_today)/self.EURO_RATE)
                return(answer+' {:.2f} Euro'.format(remains))

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        get_calories_today=(self.get_today_stats())
        if get_calories_today<self.limit:
            remains=self.limit-get_calories_today
            return('Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {} кКал'.format(remains))
        else:
            return('Хватит есть!')




if __name__=='__main__':
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=150, comment="Test 37", date="01.9.2019"))
    cash_calculator.add_record(Record(amount=145, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    cash_calculator.add_record(Record(amount=145, comment="Безудержный шопинг", date="08.03.2019"))
    cash_calculator.add_record(Record(amount=1568, comment="Наполнение потребительской корзины", date="09.03.2019"))
    cash_calculator.add_record(Record(amount=691, comment="Катание на такси", date="08.03.2019"))
    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(cash_calculator.get_today_cash_remained("eur"))
    print('Сегодня потрачено',cash_calculator.get_today_stats())
    cash_calculator.add_record(Record(amount=555, comment="Продукты"))
    print(cash_calculator.get_today_cash_remained("rub"))
    print('Сегодня потрачено',cash_calculator.get_today_stats())
    cash_calculator.add_record(Record(amount=7500, comment="Монитор"))
    print(cash_calculator.get_today_cash_remained("rub"))
    print(cash_calculator.get_today_cash_remained("usd"))
    print(cash_calculator.get_today_cash_remained("eur"))
    print('Сегодня потрачено',cash_calculator.get_today_stats())
    print('За неделю потрачено',cash_calculator.get_week_stats())
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="05.04.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="04.04.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="03.04.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="02.04.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="01.04.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="31.03.2020"))
    cash_calculator.add_record(Record(amount=1000, comment="Продукты", date="30.03.2020"))
    cash_calculator.add_record(Record(amount=1000000, comment="Продукты", date="29.03.2020"))
    cash_calculator.add_record(Record(amount=1000000, comment="Продукты", date="28.03.2020"))
    print('За неделю потрачено',cash_calculator.get_week_stats())

    calories_calculator = CaloriesCalculator(2000)
    calories_calculator.add_record(Record(amount=145, comment="кофе"))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=500, comment="творог"))
    calories_calculator.add_record(Record(amount=500, comment="йогурт"))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=855, comment="торт"))
    print(calories_calculator.get_calories_remained())
    calories_calculator.add_record(Record(amount=855, comment="торт"))
    print(calories_calculator.get_calories_remained())
    print('За неделю съедено',calories_calculator.get_week_stats())
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="05.04.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="04.04.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="03.04.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="02.04.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="01.04.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="31.03.2020"))
    calories_calculator.add_record(Record(amount=1000, comment="Продукты", date="30.03.2020"))
    calories_calculator.add_record(Record(amount=1000000, comment="Продукты", date="29.03.2020"))
    calories_calculator.add_record(Record(amount=1000000, comment="Продукты", date="28.03.2020"))
    print('За неделю съедено',calories_calculator.get_week_stats())
