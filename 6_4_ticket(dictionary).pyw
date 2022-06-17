
while (True):
    option_1=print("1.Добавить новое слово")
    option_2=print("2.Искать слово в словаре")
    choice=input("Введите 1 или 2: ")

    if (choice=="1"):
        word=input("Введите слово: ")
        translation=input("Введите перевод: ")
        file=open("D:\dict.txt","a")
        file.write(word+"             "+translation+"\n")
        closing_of_file=input("ЭТО ПОСЛЕДНЕЕ СЛОВО?: y/n ")
        if (closing_of_file=="y"):
            file.close()
            break
        elif (closing_of_file=="n"):
            continue
        else:
            print("НЕ ЯСНО!")

    elif (choice=="2"):
        word=input("Введите слово для поиска: ")
        file=open("D:\dict.txt","r")
        for line in file:
            if word in line:
                print("Найдено слово: "+line)
        
    else:
        print("Вы ввели что-то не то!")

