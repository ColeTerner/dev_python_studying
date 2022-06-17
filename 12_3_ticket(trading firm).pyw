#ФУНКЦИЯ ПОКУПКИ
def buy(item,number):
    if item==goods[0]:
        cost=prices[0]
    elif item==goods[1]:
        cost=prices[1]
    elif item==goods[2]:
        cost=prices[2]
    elif item==goods[3]:
        cost=prices[3]
    elif item==goods[4]:
        cost=prices[4]
    price=cost*int(number)
    return price

#СПИСОК ТОВАРОВ
from ast import While


el_1="pencil"
el_2="paper"
el_3="pen"
el_4="stapler"
el_5="folder"

goods=[el_1,el_2,el_3,el_4,el_5]
print("Список доступных к покупке товаров: "+str(goods))

#СПИСОК ЦЕН

price_1=100
price_2=250
price_3=125
price_4=150
price_5=25

prices=[price_1,price_2,price_3,price_4,price_5]
print("Цены на соответствующие товары:     "+str(prices))

exodus=0
#ВЫБОР ПОКУПАТЕЛЯ
while True:
    choice=input("Что именно вы желаете приобрести? - ")
    numb=input("Введите количество: ")

    exodus=exodus+buy(choice,numb)
    #РАССЧЕТ СКИДОК
    if ((exodus>=1001) and (exodus<=3000)):
        exodus=exodus-0.05*exodus
    elif (exodus>3000):
        exodus=exodus-0.07*exodus
    print(exodus)

    #Предложить купить ещё что-то?
    print("Would you like to buy anything else? : y/n")
    choice_1=input()
    if choice_1=="y":
        continue
    else:
        break







