# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()

fruits = ["яблоко", "банан", "киви", "арбуз"]

for number, fruit in enumerate(fruits, 1):
    print('{:>30} {}'.format(number, fruit))

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
lst1 = set(list1)
lst2 = set(list2)
a = lst1.difference(lst2)
a = list(a)
print(a)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.


test_list1 = [5, 6, 7, 3, 4, 5, 6, 4, 5, 6]

a = []  # новый список для записи
for i in test_list1:
    if i % 2 == 0:
        i = i / 4
        a.append(i)
    else:
        i = int(i * 2)
        a.append(i)
print(a)
