def how_much_of_fuel(money,type):
    cost_76=35.43
    cost_92=45.78
    cost_96=56.34
    if type=="92":
        exodus_92=round(money/cost_92,1)
        print(exodus_92)
    elif type=="76":
        exodus_76=round(money/cost_76,1)
        print(exodus_76)
    else:
        print("По умолчанию выбор 96")
        exodus_96=round(money/cost_96,1)
        print(exodus_96)

def how_much_of_money(litres,type):
    cost_76=35.43
    cost_92=45.78
    cost_96=56.34
    if type=="92":
        exodus_92=round(litres*cost_92,1)
        print(exodus_92)
    elif type=="76":
        exodus_76=round(litres*cost_76,1)
        print(exodus_76)
    else:
        print("По умолчанию выбор 96")
        exodus_96=round(litres*cost_96,1)
        print(exodus_96)

print("Выберите функцию:")
print("1.Рассчитать количество бензина")
print("2.Рассчитать необходимое количество денег для покупки")

choice=input("Введите 1 или 2: ")
if choice=="1":
    user_money=float(input("Сколько у вас денег: "))
    type_of_fuel=input("Тип бензина? ")
    how_much_of_fuel(user_money,type_of_fuel)
elif choice=="2":
    user_fuel=int(input("Сколько литров бензина вы хотите приобрести: "))
    type_of_fuel=input("Тип бензина? ")
    how_much_of_money(user_fuel,type_of_fuel)
else:
    print("Вы ввели что-то другое. Попробуйте снова! ")

