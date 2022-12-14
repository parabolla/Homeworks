# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math

test_list1 = [2, -5, 8, 9, -25, 25, 4]
a = []  # новый список для записи
for i in test_list1:
    m = test_list1.index(i)  # проход по индексам
    if i < 0:
        continue
    else:
        # if round(math.sqrt(i), 1) != float:
        if math.isqrt(i) ** 2 == i:
            i = round(math.sqrt(i))
            a.append(i)
        else:
            continue

print(a)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
import datetime

d = datetime.date(2013, 2, 2)

months_dict = {
    1: "Января",
    2: "Февраля",
    3: "Марта",
    4: "Апреля",
    5: "Мая",
    6: "и т.д."

}

days_dict = {
    1: "Первое",
    2: "Второе",
    3: "Третье",
    4: "Четвертое",
    5: "Пятое",
    6: "и т.д.",

}

days = days_dict[d.day]
mons = months_dict[d.month]
years = (d.year)

print("{} {} {} года".format(days, mons, years))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

import random

n = int(input())

new_list = []

for i in range(n):
    one_num = random.randint(-100, 100)
    new_list.append(one_num)

print(new_list)

# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

# 1
lst = [1, 2, 4, 5, 6, 2, 5, 2]

a = set(lst)
b = list(a)
print(b)

# 2
numbers = [1, 2, 4, 5, 6, 2, 5, 2]

unique = []

for number in numbers:
    if number in unique:
        continue
    else:
        unique.append(number)

print(unique)
