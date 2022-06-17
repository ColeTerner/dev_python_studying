# 6. Расписание звонков. В учебном заведении задается начало учебного
# дня, продолжительность «пары» или урока, продолжительность
# обычного и большого перерывов (и их «место» в расписании),
# количество пар (уроково). Составить программу, которая выведет на
# экран расписание звонков на весь учебный день.


started_day_H = int(input("Начало учебного дня (часы): "))
started_day_M = int(input("Начало учебного дня (минуты): "))
lesson_continuance_M = int(input("Продолжительность урока(в минутах): ")) #Duration
time_to_break_M = int(input("Продолжительность обычного перерыва(в минутах): ")) #standartInreval
lunch_M = int(input("Продолжительность большого перерыва(в минутах): "))#bigInterval
index_lunch = int(input("Позиция большого перерыва: ")) #indexBigInterval
number_of_lessons = int(input("Кол-во уроков: ")) #countLessons
for i in range(1, number_of_lessons+1):
    print("%20s" % ("Урок №" + str(i)))
    print("Начало в", str(started_day_H)+":"+str(started_day_M))
    started_day_M += lesson_continuance_M
    if started_day_M >= 60:
        started_day_H +=  int(started_day_m/60)
        started_day_M = started_day_M%60
    print("Конец в", str(started_day_H)+":"+str(started_day_M))
    print("")
    if i != number_of_lessons:
        print("Начало перерыва в:", str(started_day_H)+":"+str(started_day_M))

        if i != index_lunch:
            started_day_M += time_to_break_M
        else:
            started_day_M += lunch_M

        if started_day_M >= 60:
            started_day_H +=  int(started_day_M/60)
            started_day_M = started_day_M%60
        print("Конец перерыва в:", str(started_day_H)+":"+str(started_day_M))
        print("")
