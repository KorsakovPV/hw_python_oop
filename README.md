# hw_python_oop
Sprint 2. Итоговый проект.

[![hw_python_oop-app workflow](https://github.com/KorsakovPV/hw_python_oop/workflows/hw_python_oop/badge.svg)](https://github.com/KorsakovPV/yamdb_final/actions)

Учебный проект. Призванный познакомить с ООП.

## Техническое задание.

Создайте два калькулятора: для подсчёта денег и калорий. Пользовательскую часть калькуляторов, их «лицо», писать не нужно, напишите только логику — отдельный класс для каждого из калькуляторов.
Калькулятор денег должен уметь:

1. Сохранять новую запись о расходах методом *add_record()*
2. Считать, сколько денег потрачено сегодня методом *get_today_stats()*
3. Определять, сколько ещё денег можно потратить сегодня в рублях, долларах или евро — метод *get_today_cash_remained(currency)*
4. Считать, сколько денег потрачено за последние 7 дней — метод *get_week_stats()*
Калькулятор калорий должен уметь:
1. Сохранять новую запись о приёме пищи метод *add_record()*
2. Считать, сколько калорий уже съедено сегодня — метод *get_today_stats()*
3. Определять, сколько ещё калорий можно/нужно получить сегодня — метод *get_calories_remained()*
4. Считать, сколько калорий получено за последние 7 дней — метод *get_week_stats()*

### В проекте применены такие принцыпы ООП как:
1. **Абстракция** для выделения в моделируемом предмете важного для решения конкретной задачи по предмету, в конечном счёте — контекстное понимание предмета, формализуемое в виде класса;
2. **Инкапсуляция** для быстрой и безопасной организации собственно иерархической управляемости: чтобы было достаточно простой команды «что делать», без одновременного уточнения как именно делать, так как это уже другой уровень управления;
3. **Наследование** для быстрой и безопасной организации родственных понятий: чтобы было достаточно на каждом иерархическом шаге учитывать только изменения, не дублируя всё остальное, учтённое на предыдущих шагах;
4. **Полиморфизм** для определения точки, в которой единое управление лучше распараллелить или наоборот — собрать воедино.

### Применены принципы разработки:
1. **DRY** Don’t repeat yourself
2. **SOLID**
   
        Single Responsibility Principle (принцип единственности ответственности)
    
        Open/Closed Principle (принцип открытости/закрытости)
   
        Liskov Substitution Principle (принцип подстановки Барбары Лисков)
   
        Interface Segregation Principle (принцип разделения интерфейса)
   
        Dependency Inversion Principle (принцип инверсии зависимостей)