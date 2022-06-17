#ВХОДНЫЕ ДАННЫЕ
length_of_dialog=int(input("Введите длину разговора в минутах: "))
code_of_city=input("Введите код города(Москва - 001, Санкт-Петербург - 002, Екатеринбург - 003): ")
day_of_week=input("Введите день недели(с маленькой буквы): ")
#Цена за минуту разговора
cost_moscow=100
cost_peterburg=70
cost_ekb=50
#Скидка
sale=10

def calc(length,city,day):
    exodus=length*city
    if (day=="суббота" or day=="воскресенье"):
        exodus=exodus - exodus*sale/100
    return exodus

if code_of_city=="001":
    result=calc(length_of_dialog,cost_moscow,day_of_week)
    print("Прибыль компании равна: "+str(result))
elif code_of_city=="002":
    result=calc(length_of_dialog,cost_peterburg,day_of_week)
    print("Прибыль компании равна: "+str(result))
else:
    print("По-умолчанию выбирается ЕКАТЕРИНБУРГ!")
    result=calc(length_of_dialog,cost_ekb,day_of_week)
    print("Прибыль компании равна: "+str(result))






