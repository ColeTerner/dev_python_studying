stroka=input("Введите строку символов с пробелами и смволами русского и английского алфавитов: ")

list=stroka.split(" ")  #Разделение строки на список элементов

number_of_words=0 #кол-во слов

#Подсчет элементов списка list
for element in list:
    number_of_words+=1

print(number_of_words)