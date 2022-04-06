# 1. Создать программный файл в текстовом формате, записать в него 
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка.

with open(r'1.txt', 'w') as file:
    while True:
        i = input()
        if i == '':
            break
        else:
            file.write(i + '\n')


# 2. Создать текстовый файл (не программно), сохранить в нём несколько
# строк, выполнить подсчёт строк и слов в каждой строке.

lines = 0
words = []
try:
    f = open('2.txt', 'r')
    for i in f:
        lines += 1
        words.append(len(i.split()))
        print("В {0} строке количество слов: {1}".format(lines, words[lines - 1]))
    print("Всего строк: {0}, слов: {1}".format(lines, sum(words)))
except IOError:
    print("Ошибка! Такого файла не существует.")
finally:
    f.close()


# 3. Создать текстовый файл (не программно). Построчно записать 
# фамилии сотрудников и величину их окладов (не менее 10 строк). 
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести
# фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.

# Пример файла:
#Иванов 23543.12
#Петров 13749.32

employes = {}
try:
    with open('3.txt', 'r', encoding="utf-8") as f:
        employes = {i.split()[0] : i.split()[1] for i in f}
    msg = "Меньше 20000 получают: "
    work_list = ", ".join([k for k in employes if float(employes[k]) < 20000])
    salary_list = [float(i) for i in list(employes.values())]
    salary = sum(salary_list) / len(employes)
    print(msg, work_list)
    print("Средняя ЗП: {0:.{1}f}".format(salary, 2))
except IOError:
    print("Ошибка! Такого файла не существует.")

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую 
# построчно данные. При этом английские числительные должны 
# заменяться на русские. Новый блок строк должен записываться в 
# новый текстовый файл.

numbers_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open('4.txt', 'r', encoding="utf-8") as f:
        lines = [line.split() for line in f]
        print(lines)
        for i in lines:
            i[0] = numbers_dict.get(i[0])
        lines = "\n".join([" ".join(i) for i in lines])
    with open('4_new.txt', 'w', encoding="utf-8") as f_new:
        f_new.write(lines)
except IOError:
    print("Ошибка чтения! Файл не найден.")

# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделённых пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить её на экран.

from random import randint

def numbers_sum(file):
    '''Подсчитывает сумму всех чисел в файле'''
    numbers_sum = []
    try:
        with open(file, 'r') as f:
            for line in f:
                line_list = line.split()
                numbers_sum += [int(i) for i in line_list]
        return sum(numbers_sum)
    except IOError:
        return "Ошибка! Файл не найден"

def numbers_gen(file):
    '''Генерирует строку чисел через пробелы в файле'''
    try:
        with open(file, 'x') as f:
            numbers = [str(i) for i in range(0, randint(2, 500), randint(1, 125))]
            f.write(" ".join(numbers))
    except IOError:
        return "Ошибка! Файл уже создан"

numbers_gen('5.txt')
numbers_sum('5.txt')

# 6. Сформировать (не программно) текстовый файл. В нём каждая 
# строка должна описывать учебный предмет и наличие лекционных, 
# практических и лабораторных занятий по предмету. Сюда должно
# входить и количество занятий. Необязательно, чтобы для каждого
# предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее 
# количество занятий по нему. Вывести его на экран.

# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —

# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

lessons = []
hours = []
try:
    with open('6.txt', 'r', encoding='utf-8') as file:
        for line in file:
            lessons.append(''.join(line.split(':')[0]))
            nums_of_line = ''.join((num if num in '0123456789' else ' ') for num in line)
            hours.append([int(i) for i in nums_of_line.split()])
    dict_of_lessons = {lessons[i]: sum(hours[i]) for i in range(len(lessons))}
    print(dict_of_lessons)
except IOError:
    print("Ошибка! Файл не найден")

# 7. Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, 
# форма собственности, выручка, издержки.

# Пример строки файла: firm_1 ООО 10000 5000.

# Необходимо построчно прочитать файл, вычислить прибыль каждой 
# компании, а также среднюю прибыль. Если фирма получила убытки, 
# в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами 
# и их прибылями, а также словарь со средней прибылью. Если фирма
# получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.

# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

try:
    with open('7.txt', 'r', encoding='utf-8') as f:
        list_of_lines = [i.rstrip('\n').split() for i in [i for i in f]]
        dict_of_inc = {i[0]: (int(i[-2]) - int(i[-1])) for i in list_of_lines}
        count_of_inc = sum(1 for v in dict_of_inc.values() if v >= 0)
        profit_price = round((sum([v for v in dict_of_inc.values() if v >= 0]) / count_of_inc), 2)
        profit = {"average_profit": profit_price}
        data = [dict_of_inc, profit]
    with open('7.json', 'w') as f:
        json.dump(data, f)
except IOError:
    print('Ошибка! Файл не найден')