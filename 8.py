# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать 
# дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
# метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, 
# год и преобразовывать их тип к типу «Число». Второй, с декоратором 
# @staticmethod, должен проводить валидацию числа, месяца и года (например, 
# месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date):
        Date.date = date

    @classmethod
    def date_out(cls):
        return [int(i) for i in cls.date.split('-')]
    
    @staticmethod
    def date_valid():
        day, month, year = Date.date_out()
        months_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if(year % 400 == 0 or year % 100 != 0) and year % 4 == 0:
            months_day[2] = 29
        return "Корректная дата" if (1 <= month <= 12 and 1 <= day <= months_day[month]) else "Некорректная дата"

correct = Date("08-04-2012")
print(correct.date_out())
print(correct.date_valid())
print(Date("29-02-2022").date_valid())
print(Date("742-3-1970").date_valid())
print(Date("12-21-1221").date_valid())

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на
# ноль. Проверьте его работу на данных, вводимых пользователем. При вводе нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не 
# завершиться с ошибкой.

class MyDivisionZeroError(Exception):
    def __init__(self, text):
        self.txt = text

while True :
    try:
        i = float(input("Введите число: "))
        if i == 0:
            raise MyDivisionZeroError("Ошибка! Деление на ноль!")
    except MyDivisionZeroError as mdze:
        print(mdze)
    except ValueError:
        print("Некорреткное значение")
    else:
        print(1 / i)
        break

# 3. Создайте собственный класс-исключение, который должен проверять содержимое
# списка на наличие только чисел. Проверить работу исключения на реальном 
# примере. Запрашивать у пользователя данные и заполнять список необходимо 
# только числами. Класс-исключение должен контролировать типы данных элементов
# списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, 
# пока пользователь сам не остановит работу скрипта, введя, например, команду 
# «stop». При этом скрипт завершается, сформированный список с числами выводится
# на экран.

# Подсказка: для этого задания примем, что пользователь может вводить только 
# числа и строки. Во время ввода пользователем очередного элемента необходимо 
# реализовать проверку типа элемента. Вносить его в список, только если введено
# число. Класс-исключение должен не позволить пользователю ввести текст (не число)
# и отобразить соответствующее сообщение. 
# При этом работа скрипта не должна завершаться.

class MyValueError(ValueError):
    def __init__(self, text):
        self.text = text

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

res = []
while True:
    try:
        value = input("Введите число: ")
        if value == "stop":
            break
        if not is_float(value):
            raise MyValueError("Некорректный ввод")
        res.append(value)
    except MyValueError as mve:
        print(mve)

print(res)


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
# склад. А также класс «Оргтехника», который будет базовым для 
# классов-наследников. Эти классы — конкретные типы оргтехники (принтер,
# сканер, ксерокс). В базовом классе определите параметры, общие для 
# приведённых типов. В классах-наследниках реализуйте параметры, уникальные 
# для каждого типа оргтехники.

class Warehouse:
    def __init__(self):
        self.__all = {}

    def add(self, equipment):
        '''Добавить на склад технику'''

        self.__all.setdefault(equipment.unification(), []).append(equipment)

    def get(self, kind_of):
        '''Убрать со склада технику'''

        self.__all.setdefault(kind_of).pop(0)

    def show(self):
        '''Вывести количество техники'''

        return f'{self.__all}'

class Equipment:
    def __init__(self, model):
        self.model = model
        self.kind = self.__class__.__name__

    def unification(self):
        '''Возвращает имя класса'''

        return f'{self.kind}'

    def __repr__(self):
        '''Возвращает модель'''

        return f'{self.model}'

class Printer(Equipment):
    def __init__(self, serial_number, model):
        super().__init__(model)
        self.serial_number = serial_number

    def __repr__(self):
        return f'S/N:{self.serial_number} ({self.model})'

class Scanner(Equipment):
    def __init__(self, model, working=True):
        super().__init__(model)
        self.working = working

    def __repr__(self):
        return f'Рабочий?: {self.working} ({self.model})'

class Copier(Equipment):
    def __init__(self, model):
        super().__init__(model)

    def __repr__(self):
        return f'{self.model}'

warehouse = Warehouse()
printer_1 = Printer("A2SDD466H8", "HP")
printer_3 = Printer("X34567234JKL9", "Xerox")
warehouse.add(printer_1)
warehouse.add(Printer("434D099G07", "HP"))
warehouse.add(printer_3)
scanner_1 = Scanner("HP")
scanner_2 = Scanner("Sumsung", False)
warehouse.add(scanner_1)
warehouse.add(scanner_2)
copier = Copier("Xerox")
warehouse.add(copier)

print(warehouse.show())
warehouse.get("Printer")
print(warehouse.show())

# 5. Продолжить работу над первым заданием. Разработайте методы, которые 
# отвечают за приём оргтехники на склад и передачу в определённое подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники, 
# а также других данных, можно использовать любую подходящую структуру 
# (например, словарь).

class Warehouse:
    def __init__(self):
# Инициализация структуры компании по отделам
        self.__all_of = {"Склад": {},
                         "Мордор": {},
                         "Пещера Голлума": {},
                         "Почта PPH": {}}

    def add(self, equipment, place="Склад"):
        self.__all_of[place].setdefault(equipment.unification(), []).append(equipment)
        
    def get(self, kind_of, place="Склад"):
        return self.__all_of[place].setdefault(kind_of).pop(0)
        
    def transfer(self, kind_of, from_place="Склад", to_place="Мордор"):
# Передача техники из одного отдела в другой(по умолчанию со Склада в Мордор)'''
        self.add(self.get(kind_of, from_place), to_place)
    
    def how_match(self, kind_of, place="Склад"):
# Подсчет количества техники в указанном отделе
        return f'{len(self.__all_of[place][kind_of])}'
    
    def all_of(self):
# Вывод полного списка техники всей компании
        for i in self.__all_of:
            print(f'{i}: {self.__all_of[i]}')
        return True
        
    def show(self, place="Склад"):
# Вывод техники конкретного отдела
        if place in self.__all_of.keys():
            return f'{self.__all_of[place]}'
        else:
            return 'Некорректные данные'


warehouse.transfer("Printer")
print(warehouse.show(), warehouse.show("Мордор"))
print(warehouse.all_of())
print(warehouse.how_match("Printer"))
print(warehouse.how_match("Printer", "Мордор"))
warehouse.transfer("Printer", "Мордор", "Пещера Голлума")
print(warehouse.show("Пещера Голлума"))
print(warehouse.all_of())

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации 
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум 
# возможностей, изученных на уроках по ООП.

class Warehouse:
    def __init__(self):
        self.__all_of = {"Склад": {},
                         "Мордор": {},
                         "Пещера Голлума": {},
                         "Почта PPH": {}}

    def add(self, equipment, place="Склад"):
#6 Добавляем валидацию на тип данных
        try:
            if not isinstance(equipment, Equipment):
                raise Exception()
            else:
                self.__all_of[place].setdefault(equipment.unification(), []).append(equipment)
        except:
            print("Некорректные данные")
        
    def get(self, kind_of, place="Склад"):
#6 Добавляем валидацию на нахождение техники
        try:
            if kind_of not in self.__all_of[place]:
                raise Exception()
            else:
                return self.__all_of[place].setdefault(kind_of).pop(0)
        except:
            print(f"Такой техники нет на {place}")
        
    def transfer(self, kind_of, from_place="Склад", to_place="Мордор"):
        self.add(self.get(kind_of, from_place), to_place)
    
    def how_match(self, kind_of, place="Склад"):
        return f'{len(self.__all_of[place][kind_of])}'
    
    def all_of(self):
        for i in self.__all_of:
            print(f'{i}: {self.__all_of[i]}')
        return True
        
    def show(self, place="Склад"):
#6 Вывод техники конкретного отдела
        if place in self.__all_of.keys():
            return f'{self.__all_of[place]}'
        else:
            return 'Такого отдела нет '

warehouse.add(1)
warehouse.get("Computer")
warehouse.transfer("Excalibure")
print(warehouse.show("Riverwood"))

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс 
# «Комплексное число». Реализуйте перегрузку методов сложения и умножения 
# комплексных чисел. Проверьте работу проекта. Для этого создаёте 
# экземпляры класса (комплексные числа), выполните сложение и умножение 
# созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, a: float, b:float):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b}i'

    def __mul__(self, other):
        return f'{self.a * other.a - self.b * other.b} * {self.a * other.b + other.a * self.b}i'

    def __str__(self):
        return f'{self.a} + {self.b}i'

x = ComplexNumber(2, 3)
y = ComplexNumber(4, 5)
print(x)
print(y)
print(x + y)
print(x * y)

a = complex('2+3j')
b = complex('4+5j')
print(a)
print(b)
print(a + b)
print(a * b)
