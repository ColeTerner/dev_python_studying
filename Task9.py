#9. Составьте программу, которая выводит на экран календарь на любой
#месяц по заданному году. Воспользуйтесь алгоритмом вычисления дня
#недели, описанном в лабораторной работе 5.

from calendar import monthrange
import math
print("Программа выводит календарь за заданный год и месяц")
year = int(input("Введите год: "))
month = int(input("Введите номер месяца: "))
days_in_month = monthrange(year, month)
days = [
    [None] * 7,
    [None] * 7,
    [None] * 7,
    [None] * 7,
    [None] * 7,
    [None] * 7
]
print("%6s %4s %4s %4s %4s %4s %4s" %("Пн.", "Вт.", "Ср.", "Чт.", "Пт.", "Сб.", "Вс."))
fist_day_index = days_in_month[0]
day = 1
index = fist_day_index
for i in range(6):
    for j in range(index, 6 + 1):
        if day > days_in_month[1]:
            break
        days[i][j] = day
        day += 1
        index += 1
        if index > 6:
            index = 0
            break
for i in range(len(days)):
    for j in range(len(days[i])):
        if days[i][j] == None:
            print("%5s" % (" "), end="")
        else:
            print("%5s" % (days[i][j]), end="")
    print("")
