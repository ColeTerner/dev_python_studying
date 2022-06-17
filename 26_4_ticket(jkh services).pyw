from getpass import getpass
from mysql.connector import connect, Error




#Создание новой БД - JKH_services
create_db_service_of_jkh="CREATE DATABASE JKH_services"

try:
    with connect (
        host="localhost",
        user=input("Введите имя пользователя: "),
        password=getpass("Введите пароль БД: "),
    ) as connection:
        print(connection)
        with connection.cursor() as cursor:
            cursor.execute(create_db_service_of_jkh)
except Exception as e:
    print(e)

#СОЗДАНИЕ ТАБЛИЦЫ payment
create_table_payment="""
CREATE TABLE payment(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    room INT,
    debt FLOAT
)
"""
try:
    with connect (
        host="localhost",
        user=input("Введите имя пользователя: "),
        password=getpass("Введите пароль: "),
        database="JKH_services"
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(create_table_payment)
except Exception as e:
    print(e)


#1)ВСТАВКА ЗАПИСИ В ТАБЛИЦУ
def insert_user(name,surname,room,debt):
    print("ВСТАВКА ЗАПИСИ В ТАБЛИЦУ!")
    room=int(room)
    debt=float(debt)
    row=(name,surname,room,debt)
    insert_table_payment="""
INSERT INTO payment (name,surname,room,debt) 
VALUES
    (%s,%s,%s,%s)
""".format(name,surname,room,debt)
    
    
    try:
        with connect(
            host="localhost",
            user=input("DB username: "),
            password=getpass("Введите пароль: "),
            database="jkh_services"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(insert_table_payment,row)
                connection.commit()
    except Exception as e:
        print(e)
    
#2)ПРОСМОТР ВСЕХ ПОЛЬЗОВАТЕЛЕЙ ТАБЛИЦЫ
def show_rows():
    print("ИЗВЛЕЧЕНИЕ ЗАПИСЕЙ ИЗ ТАБЛИЦЫ!")
    select_from_payment="""
    SELECT * FROM payment
    """
    try:
        with connect(
            host="localhost",
            user=input("DB username: "),
            password=getpass("Введите пароль: "),
            database="jkh_services"
        ) as connection:
            with connection.cursor() as cursor:
                cursor.execute(select_from_payment)
                result=cursor.fetchall()
                for row in result:
                    print(row)
    except Exception as e:
        print(e)

#3)УДАЛЕНИЕ ЗАПИСИ ИЗ ТАБЛИЦЫ
# def del_row(name):
#     delete_from_payment="""
# DELETE FROM payment 
# WHERE payment.name=%s
# """.format(name)
#     try:
#         with connect(
#             host="localhost",
#             user=input("Введите пароль пользователя БД: "),
#             password=getpass("Введите пароль: "),
#             database="jkh_services"
#         ) as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute(delete_from_payment)
#                 connection.commit()
#     except Exception as e:
#         print(e)

#4)АПДЕЙТ ЗАПИСИ
# def update_row(name,surname,room,debt,old_name):
#     print("АПДЕЙТ ЗАПИСИ В ТАБЛИЦЕ!")
#     room=int(room)
#     debt=float(debt)
#     row=(name,surname,room,debt,old_name)
#     update_table_payment="""
# UPDATE payment 
# SET name=%s, 
# surname=%s, 
# WHERE name=%s
# """.format(name,surname,room,debt,old_name)

#     try:
#         with connect(
#             host="localhost",
#             user=input("Введите пользователя DB: "),
#             password=getpass("Введите пароль: "),
#             database="jkh_services"
#         ) as connection:
#             with connection.cursor() as cursor:
#                 cursor.execute(update_table_payment)
#                 connection.commit()
#     except Exception as e:
#         print(e)
    

#НАЧАЛО ПРОГРАММЫ
print("1.Заведение нового жильца в БД")
print("2.Просмотр всех записей жильцов из БД")
# print("3.Удалить жильца из БД")
# print("4.Обновить запись о жильце")
choice=input("Выберите действие для работы с БД(1/2):")         #3,4


if choice=="1":
    payment_name=input("Введите имя жильца: ")
    payment_surname=input("Введите фамилию жильца: ")
    payment_room=input("Введите номер квартиры жильца: ")
    payment_debt=input("Введите долг жильца: ")
    insert_user(payment_name,payment_surname,payment_room,payment_debt)
elif choice=="2":
    show_rows()
# elif choice=="3":
#     payment_name=input("Введите имя удаляемого жильца: ")
#     del_row(payment_name)
# elif choice=="4":
#     payment_name=input("Введите имя жильца: ")
#     payment_surname=input("Введите фамилию жильца: ")
#     payment_room=input("Введите номер квартиры жильца: ")
#     payment_debt=input("Введите долг жильца: ")
#     payment_old_name=input("Введите прежнее имя владельца: ")
#     update_row(payment_name,payment_surname,payment_room,payment_debt,payment_old_name)



